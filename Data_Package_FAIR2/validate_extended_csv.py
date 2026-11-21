#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation script for Compound_Properties_Experimental_Extended.csv
Checks:
- Valid placeholder format (NR, NA, ND, EST - uppercase only)
- Header consistency with main database
- Basic data integrity:
  - every record has as many fields as the header, counted with csv.reader
    (pandas pads a short record with empty cells and leaves its last values
    in the wrong columns, without any error)
  - no empty cell and no missing-value marker that pandas reads as NaN by
    default (N/A, null, None, NaN...): missing values use NA, ND, NR or EST

Placeholder and header errors always fail (exit status 1). Data integrity
findings are warnings by default and fail with --strict:

    python validate_extended_csv.py           # warnings only, exit status 0
    python validate_extended_csv.py --strict  # exit status 1 on any finding

The CSV is loaded with keep_default_na=False, so the NA placeholder stays the
string "NA" instead of becoming NaN like an empty cell. A record with more
fields than the header cannot be loaded by pandas, which fails in both modes.
"""

import argparse
import csv
import sys

import pandas as pd

EXTENDED_CSV = 'Compound_Properties_Experimental_Extended.csv'
MAIN_CSV = 'Compound_Properties_Database.csv'
VALID_PLACEHOLDERS = {'NR', 'NA', 'ND', 'EST'}
# Strings that pandas.read_csv reads as NaN by default, except '' (reported as
# an empty cell) and 'NA' (a valid placeholder).
NON_STANDARD_MISSING = {
    '#N/A', '#N/A N/A', '#NA', '-1.#IND', '-1.#QNAN', '-NaN', '-nan',
    '1.#IND', '1.#QNAN', '<NA>', 'N/A', 'NULL', 'NaN', 'None', 'n/a',
    'nan', 'null',
}


def read_records(path):
    """Read a CSV file with csv.reader and return (header, records).

    records lists (line, fields) for each data record, where line is the
    physical line on which the record starts. Blank lines are skipped, as
    pandas does.
    """
    header = None
    records = []
    with open(path, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        line = 1
        for fields in reader:
            if fields:
                if header is None:
                    header = fields
                else:
                    records.append((line, fields))
            line = reader.line_num + 1
    return header, records


def field_count_findings(header, records):
    """Return (line, message) for each record whose field count differs from the header."""
    return [
        (line, f'{len(fields)} fields, header has {len(header)} '
               f'(record starts with "{fields[0]}")')
        for line, fields in records
        if len(fields) != len(header)
    ]


def missing_value_findings(header, records):
    """Return (line, message) for each empty cell or non-standard missing value.

    Records with a wrong field count are skipped: their values are not in
    their columns, and field_count_findings already reports them.
    """
    findings = []
    for line, fields in records:
        if len(fields) != len(header):
            continue
        for column, value in zip(header, fields):
            if not value.strip():
                findings.append(
                    (line, f'empty cell in column {column} (use NA, ND, NR or EST)'))
            elif value.strip() in NON_STANDARD_MISSING:
                findings.append(
                    (line, f'non-standard missing value "{value}" in column {column} '
                           '(use NA, ND, NR or EST)'))
    return findings


def load_dataframe(path):
    """Load a CSV with pandas, keeping the NA placeholder as the string "NA"."""
    return pd.read_csv(path, keep_default_na=False)


def format_lines(findings):
    """Return the line numbers of findings, sorted, as '15, 16, 17'."""
    return ', '.join(str(line) for line in sorted({line for line, _ in findings}))


def main(extended_csv=EXTENDED_CSV, main_csv=MAIN_CSV, strict=False):
    """Run validation checks on Extended CSV.

    Exits with status 1 if the file cannot be read, if a placeholder or
    header check fails, or, when strict is True, if a data integrity check
    reports a finding.
    """
    level = 'ERROR' if strict else 'WARNING'
    errors = []
    warnings = []

    # Count fields record by record, before pandas pads short records
    try:
        header, records = read_records(extended_csv)
    except (OSError, UnicodeError, csv.Error) as e:
        print(f'[ERROR] Failed to read Extended CSV: {e}')
        sys.exit(1)
    if header is None:
        print('[ERROR] Extended CSV is empty')
        sys.exit(1)

    integrity_checks = [
        ('field count differs from the header',
         field_count_findings(header, records),
         f'All {len(records)} records have {len(header)} fields'),
        ('empty or non-standard missing value',
         missing_value_findings(header, records),
         'No empty cell or non-standard missing value'),
    ]
    for problem, findings, ok_message in integrity_checks:
        for line, message in findings:
            print(f'[{level}] Line {line}: {message}')
        if findings:
            warnings.append(f'{problem} on line(s) {format_lines(findings)}')
        else:
            print(f'[OK] {ok_message}')

    # Load Extended CSV
    try:
        df = load_dataframe(extended_csv)
        print(f'[OK] Extended CSV loaded: {len(df)} rows')
    except Exception as e:
        print(f'[ERROR] Failed to load Extended CSV: {e}')
        sys.exit(1)

    # Check valid placeholders
    invalid_found = False

    for col in df.columns:
        for idx, val in enumerate(df[col]):
            if isinstance(val, str):
                val_upper = val.strip().upper()
                # Check for invalid lowercase or mixed case placeholders
                if val_upper in VALID_PLACEHOLDERS and val.strip() != val_upper:
                    print(
                        f'[ERROR] Row {idx+2}, Column {col}: '
                        f'Invalid placeholder case "{val}" (should be uppercase)'
                    )
                    invalid_found = True

    if invalid_found:
        errors.append('invalid placeholder case')
    else:
        print('[OK] All placeholders use valid uppercase format (NR/NA/ND/EST)')

    # Check header consistency with main database
    try:
        df_main = pd.read_csv(main_csv)
        if list(df.columns) != list(df_main.columns):
            print('[ERROR] Extended CSV headers do not match main database')
            print(f'  Extended: {list(df.columns)[:5]}...')
            print(f'  Main: {list(df_main.columns)[:5]}...')
            errors.append('headers do not match main database')
        else:
            print('[OK] Extended CSV headers match main database')
    except Exception as e:
        print(f'[WARNING] Could not compare headers: {e}')

    if strict:
        errors.extend(warnings)
        warnings = []
    if errors:
        print(f'\n[ERROR] Validation failed: {"; ".join(errors)}')
        sys.exit(1)
    if warnings:
        print(f'\n[OK] Validation passed with warnings: {"; ".join(warnings)} '
              '(use --strict to make them fail)')
    else:
        print('\n[OK] Validation passed')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Validate Compound_Properties_Experimental_Extended.csv '
                    '(run from Data_Package_FAIR2).')
    parser.add_argument(
        '--strict', action='store_true',
        help='fail (exit status 1) on data integrity findings instead of '
             'reporting them as warnings')
    main(strict=parser.parse_args().strict)
