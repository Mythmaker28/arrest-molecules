#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dataset status report for the Molecular Arrest data package.

Reports, as read from the files themselves:
- row counts of the core and extended CSV datasets
- rows whose number of fields differs from the header
- the stored Confidence_Grade values
- placeholder and missing-value totals (NR, NA, ND, EST, empty cells)
- the quality-tier distribution documented in DATA_QUALITY_OVERVIEW.md
  (tiers are not stored in the CSV files)

The report only reads files; it never modifies them.

Usage:
    python dataset_status.py
"""

import csv
import re
import sys
from collections import Counter
from pathlib import Path

DATA_DIR = Path(__file__).parent
CORE_CSV = DATA_DIR / 'Compound_Properties_Database.csv'
EXTENDED_CSV = DATA_DIR / 'Compound_Properties_Experimental_Extended.csv'
QUALITY_OVERVIEW = DATA_DIR / 'DATA_QUALITY_OVERVIEW.md'

PLACEHOLDERS = ['NR', 'NA', 'ND', 'EST']


def csv_status(csv_path):
    """
    Summarise a CSV dataset without interpreting its values.

    Cells are compared verbatim (after stripping spaces), so "NA" is
    counted as a placeholder and never converted to a missing value.

    Returns:
    --------
    dict : rows, columns, blank_lines, short_rows, long_rows, names,
           confidence_grades, missing (placeholder and empty-cell counts)
           and absent (fields missing from short rows)
    """
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        records = []
        blank_lines = 0
        for row in reader:
            if row:
                records.append((reader.line_num, row))
            else:
                blank_lines += 1

    n_columns = len(header)
    grade_index = header.index('Confidence_Grade') if 'Confidence_Grade' in header else None

    missing = Counter({key: 0 for key in PLACEHOLDERS + ['empty']})
    grades = Counter()
    short_rows, long_rows = [], []
    absent = 0

    for line, row in records:
        if len(row) < n_columns:
            short_rows.append((line, row[0], len(row)))
            absent += n_columns - len(row)
        elif len(row) > n_columns:
            long_rows.append((line, row[0], len(row)))

        for value in row:
            value = value.strip()
            if value in PLACEHOLDERS:
                missing[value] += 1
            elif value == '':
                missing['empty'] += 1

        if grade_index is not None:
            grades[row[grade_index].strip() if grade_index < len(row) else '(field absent)'] += 1

    return {
        'rows': len(records),
        'columns': n_columns,
        'blank_lines': blank_lines,
        'short_rows': short_rows,
        'long_rows': long_rows,
        'names': [row[0] for _, row in records],
        'confidence_grades': grades,
        'missing': missing,
        'absent': absent,
    }


def documented_tiers(overview_path):
    """
    Read the tier assignments from the "Data Quality Tiers" section of
    DATA_QUALITY_OVERVIEW.md, i.e. headings such as
    "### Tier A ..." followed by "#### 1. Salvinorin A [CORE]".

    Returns:
    --------
    list of (tier, compound, dataset) with dataset 'core' or 'extended'
    """
    entries = []
    tier = None
    in_section = False
    for line in Path(overview_path).read_text(encoding='utf-8').splitlines():
        if line.startswith('## '):
            in_section = line.strip() == '## Data Quality Tiers'
            tier = None
            continue
        if not in_section:
            continue
        match = re.match(r'###\s+Tier\s+([A-Z])\b', line)
        if match:
            tier = match.group(1)
            continue
        match = re.match(r'####\s+\d+\.\s+(.+?)\s+\[(CORE|EXTENDED)\]\s*$', line)
        if match and tier:
            entries.append((tier, match.group(1), match.group(2).lower()))
    return entries


def normalise_name(name):
    """Compare compound names without case or a trailing alias, e.g. "Everolimus (RAD001)"."""
    return re.sub(r'\s*\([^)]*\)\s*$', '', name).strip().lower()


def compare_tiers(entries, names_by_dataset):
    """
    Cross-check documented tiers against the CSV compound names.

    Returns:
    --------
    dict : 'undocumented' maps each dataset to its CSV compounds without a
           documented tier; 'not_found' lists the documented (tier, compound,
           dataset) entries absent from that dataset's CSV
    """
    documented = {}
    for tier, compound, dataset in entries:
        documented.setdefault(dataset, set()).add(normalise_name(compound))

    undocumented = {
        dataset: [name for name in names if normalise_name(name) not in documented.get(dataset, set())]
        for dataset, names in names_by_dataset.items()
    }
    not_found = [
        (tier, compound, dataset) for tier, compound, dataset in entries
        if normalise_name(compound) not in {normalise_name(n) for n in names_by_dataset.get(dataset, [])}
    ]
    return {'undocumented': undocumented, 'not_found': not_found}


def format_counts(counter):
    return ', '.join(f'{key} {count}' for key, count in counter.items()) or 'none'


def print_csv_status(label, csv_path, status):
    print(f'{label} ({Path(csv_path).name})')
    print(f'  Rows: {status["rows"]} ({status["columns"]} columns)')
    if status['blank_lines']:
        print(f'  Blank lines skipped: {status["blank_lines"]}')
    for title, rows in (('fewer', status['short_rows']), ('more', status['long_rows'])):
        if rows:
            print(f'  Rows with {title} fields than the header: {len(rows)}')
            for line, name, n_fields in rows:
                print(f'    line {line}: {name} ({n_fields} of {status["columns"]} fields)')
    grades = dict(sorted(status['confidence_grades'].items(), key=lambda item: (-item[1], item[0])))
    print(f'  Confidence_Grade values: {format_counts(grades)}')
    missing = status['missing']
    print(f'  Placeholders: NR {missing["NR"]}, NA {missing["NA"]}, ND {missing["ND"]}, EST {missing["EST"]}')
    print(f'  Empty cells: {missing["empty"]}; fields absent from short rows: {status["absent"]} '
          f'(of {status["rows"] * status["columns"]} cells)')


def main(core_csv=CORE_CSV, extended_csv=EXTENDED_CSV, overview=QUALITY_OVERVIEW):
    """Print the status report; exit with code 1 if a file cannot be read."""
    try:
        core = csv_status(core_csv)
        extended = csv_status(extended_csv)
        entries = documented_tiers(overview)
    except (OSError, StopIteration, UnicodeDecodeError, csv.Error) as e:
        print(f'[ERROR] Could not read the data package: {e!r}')
        sys.exit(1)

    print('=' * 60)
    print('DATASET STATUS')
    print('=' * 60)
    print_csv_status('Core dataset', core_csv, core)
    print()
    print_csv_status('Extended dataset', extended_csv, extended)
    print(f'\nTotal rows: {core["rows"] + extended["rows"]} (core {core["rows"]}, extended {extended["rows"]})')

    print(f'\nQuality tiers documented in {Path(overview).name} (not stored in the CSV files)')
    for tier in sorted({tier for tier, _, _ in entries}):
        datasets = Counter(dataset for t, _, dataset in entries if t == tier)
        print(f'  Tier {tier}: {sum(datasets.values())} (core {datasets["core"]}, extended {datasets["extended"]})')
    datasets = Counter(dataset for _, _, dataset in entries)
    print(f'  Total: {len(entries)} (core {datasets["core"]}, extended {datasets["extended"]})')

    check = compare_tiers(entries, {'core': core['names'], 'extended': extended['names']})
    for dataset, names in check['undocumented'].items():
        print(f'  {dataset.capitalize()} rows without a documented tier: {len(names)}'
              + (f' ({", ".join(names)})' if names else ''))
    print(f'  Documented compounds not found in their CSV: {len(check["not_found"])}'
          + (' (' + ', '.join(f'{c} [{d}, Tier {t}]' for t, c, d in check['not_found']) + ')'
             if check['not_found'] else ''))
    print('=' * 60)


if __name__ == '__main__':
    main()
