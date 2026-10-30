import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

import pandas as pd

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent))

from dataset_status import (CORE_CSV, EXTENDED_CSV, QUALITY_OVERVIEW, compare_tiers, csv_status,
                            documented_tiers, main)

FIXTURE_CSV = (
    'Compound_Name,K_d_nM,Confidence_Grade\n'
    'Alpha,1.0,HIGH\n'
    'Beta,NR,EST\n'
    'Gamma,NA,\n'
    'Delta,ND\n'
    '\n'
    'Epsilon,2.0,LOW,extra\n'
)

FIXTURE_OVERVIEW = """# Overview
## Summary Statistics
### Tier Z - outside the tier section
#### 1. Outside [CORE]
## Data Quality Tiers
### Tier A - Core
#### 1. Alpha [CORE]
Justification text
#### 2. Beta (B-1) [EXTENDED]
### Tier B - Moderate
#### 3. Gamma [EXTENDED]
## Another Section
#### 4. Delta [CORE]
"""


class TestDatasetStatusFixtures(unittest.TestCase):
    """Counts on small hand-written files with known answers."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp_dir = Path(tmp.name)

    def write(self, name, text):
        path = self.tmp_dir / name
        path.write_text(text, encoding='utf-8')
        return path

    def test_csv_status_counts(self):
        status = csv_status(self.write('fixture.csv', FIXTURE_CSV))
        self.assertEqual(status['rows'], 5)
        self.assertEqual(status['columns'], 3)
        self.assertEqual(status['blank_lines'], 1)
        self.assertEqual(status['short_rows'], [(5, 'Delta', 2)])
        self.assertEqual(status['long_rows'], [(7, 'Epsilon', 4)])
        self.assertEqual(status['absent'], 1)
        # "NA" is a placeholder here, not a missing value
        self.assertEqual(dict(status['missing']), {'NR': 1, 'NA': 1, 'ND': 1, 'EST': 1, 'empty': 1})
        self.assertEqual(dict(status['confidence_grades']),
                         {'HIGH': 1, 'EST': 1, '': 1, '(field absent)': 1, 'LOW': 1})

    def test_documented_tiers_reads_only_the_tier_section(self):
        entries = documented_tiers(self.write('overview.md', FIXTURE_OVERVIEW))
        self.assertEqual(entries, [('A', 'Alpha', 'core'),
                                   ('A', 'Beta (B-1)', 'extended'),
                                   ('B', 'Gamma', 'extended')])

    def test_compare_tiers_matches_aliases(self):
        entries = [('A', 'Everolimus', 'extended'), ('B', 'Missing', 'core')]
        check = compare_tiers(entries, {'core': ['Alpha'],
                                        'extended': ['Everolimus (RAD001)', 'Zolpidem']})
        self.assertEqual(check['undocumented'], {'core': ['Alpha'], 'extended': ['Zolpidem']})
        self.assertEqual(check['not_found'], [('B', 'Missing', 'core')])

    def test_missing_file_exits_with_error(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), self.assertRaises(SystemExit) as cm:
            main(core_csv=self.tmp_dir / 'missing.csv')
        self.assertEqual(cm.exception.code, 1)
        self.assertIn('[ERROR]', out.getvalue())


class TestDatasetStatusPublishedData(unittest.TestCase):
    """Consistency checks on the published files, without hard-coding their counts."""

    def test_row_counts_match_pandas(self):
        for path in (CORE_CSV, EXTENDED_CSV):
            with self.subTest(path=path.name):
                self.assertEqual(csv_status(path)['rows'], len(pd.read_csv(path)))

    def test_core_rows_have_one_field_per_column(self):
        status = csv_status(CORE_CSV)
        self.assertEqual(status['short_rows'], [])
        self.assertEqual(status['long_rows'], [])

    def test_documented_tier_compounds_exist_in_their_csv(self):
        names = {'core': csv_status(CORE_CSV)['names'], 'extended': csv_status(EXTENDED_CSV)['names']}
        entries = documented_tiers(QUALITY_OVERVIEW)
        self.assertTrue(entries)
        self.assertEqual(compare_tiers(entries, names)['not_found'], [])

    def test_report_runs_on_published_data(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            main()
        total = csv_status(CORE_CSV)['rows'] + csv_status(EXTENDED_CSV)['rows']
        self.assertIn(f'Total rows: {total} ', out.getvalue())
        self.assertIn('Quality tiers documented in DATA_QUALITY_OVERVIEW.md', out.getvalue())


if __name__ == '__main__':
    unittest.main()
