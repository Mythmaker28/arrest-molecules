import contextlib
import csv
import io
import re
import sys
import tempfile
import unittest
from pathlib import Path

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent))

from validate_extended_csv import load_dataframe, main

DATA_DIR = Path(__file__).parent
EXTENDED_CSV = DATA_DIR / 'Compound_Properties_Experimental_Extended.csv'
MAIN_CSV = DATA_DIR / 'Compound_Properties_Database.csv'
# Data integrity findings are printed as '[WARNING] Line N: ...' or '[ERROR] Line N: ...'
FINDING = re.compile(r'^\[(ERROR|WARNING)\] Line (\d+):', re.MULTILINE)


class TestValidateExtendedCSV(unittest.TestCase):
    """Tests for validate_extended_csv.py. Corrupted fixtures are written to a
    temporary directory; the published CSV files are only read."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp_dir = Path(tmp.name)
        with open(MAIN_CSV, newline='', encoding='utf-8') as f:
            self.header = next(csv.reader(f))

    def fixture_rows(self):
        """Return the header and three valid records, on lines 2, 3 and 4."""
        return [list(self.header)] + [
            [f'Fixture compound {i}'] + ['NR'] * (len(self.header) - 1)
            for i in range(3)
        ]

    def write_fixture(self, rows):
        path = self.tmp_dir / 'extended_fixture.csv'
        with open(path, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f, lineterminator='\n').writerows(rows)
        return path

    def run_main(self, extended_csv, strict=False):
        """Run the validator and return (exit code, output, findings), where
        findings lists (level, line) for each data integrity finding."""
        out = io.StringIO()
        code = 0
        with contextlib.redirect_stdout(out):
            try:
                main(extended_csv, MAIN_CSV, strict=strict)
            except SystemExit as e:
                code = e.code
        output = out.getvalue()
        findings = [(level, int(line)) for level, line in FINDING.findall(output)]
        return code, output, findings

    def test_short_record_warns_by_default_and_fails_with_strict(self):
        """A record with a missing field is listed; only --strict fails on it."""
        rows = self.fixture_rows()
        del rows[2][9]  # the record on line 3 loses a field, later values shift left
        path = self.write_fixture(rows)

        code, out, findings = self.run_main(path)
        self.assertEqual(code, 0)
        self.assertEqual(findings, [('WARNING', 3)])
        self.assertIn(f'{len(self.header) - 1} fields, header has {len(self.header)}', out)
        self.assertIn('[OK] Validation passed with warnings', out)

        code, out, findings = self.run_main(path, strict=True)
        self.assertEqual(code, 1)
        self.assertEqual(findings, [('ERROR', 3)])
        self.assertNotIn('Validation passed', out)

    def test_long_record_is_listed_and_cannot_be_loaded(self):
        """A record with an extra field is listed; pandas cannot load the file."""
        rows = self.fixture_rows()
        rows[2].append('NR')
        path = self.write_fixture(rows)

        code, out, findings = self.run_main(path, strict=True)
        self.assertEqual(code, 1)
        self.assertEqual(findings, [('ERROR', 3)])

        code, out, findings = self.run_main(path)
        self.assertEqual(code, 1)
        self.assertEqual(findings, [('WARNING', 3)])
        self.assertIn('Failed to load Extended CSV', out)
        self.assertNotIn('Validation passed', out)

    def test_placeholders_are_not_missing_values(self):
        """NA, ND, NR and EST pass, even with --strict."""
        rows = self.fixture_rows()
        rows[1][9] = 'NA'
        rows[2][9] = 'ND'
        rows[3][9] = 'EST'
        code, out, findings = self.run_main(self.write_fixture(rows), strict=True)
        self.assertEqual(code, 0)
        self.assertEqual(findings, [])
        self.assertIn('[OK] Validation passed', out)

    def test_na_placeholder_is_loaded_as_a_string(self):
        """pandas keeps NA as text instead of reading it as a missing value."""
        rows = self.fixture_rows()
        rows[1][9] = 'NA'
        df = load_dataframe(self.write_fixture(rows))
        self.assertEqual(df.iloc[0, 9], 'NA')
        self.assertFalse(df.isna().any().any())

    def test_empty_and_non_standard_missing_values_are_listed(self):
        """An empty cell and markers such as N/A are listed; only --strict fails on them."""
        rows = self.fixture_rows()
        rows[1][9] = ''
        rows[3][9] = 'N/A'
        rows[3][10] = 'null'
        path = self.write_fixture(rows)

        code, out, findings = self.run_main(path)
        self.assertEqual(code, 0)
        self.assertEqual(findings, [('WARNING', 2), ('WARNING', 4), ('WARNING', 4)])
        self.assertIn(f'empty cell in column {self.header[9]}', out)
        self.assertIn(f'non-standard missing value "N/A" in column {self.header[9]}', out)

        code, out, findings = self.run_main(path, strict=True)
        self.assertEqual(code, 1)
        self.assertEqual(findings, [('ERROR', 2), ('ERROR', 4), ('ERROR', 4)])
        self.assertNotIn('Validation passed', out)

    def test_lowercase_placeholder_fails_without_reporting_success(self):
        rows = self.fixture_rows()
        rows[2][9] = 'nr'
        code, out, findings = self.run_main(self.write_fixture(rows))
        self.assertEqual(code, 1)
        self.assertIn('Invalid placeholder case "nr"', out)
        self.assertNotIn('Validation passed', out)

    def test_header_mismatch_fails(self):
        rows = self.fixture_rows()
        rows[0][-1] += '_renamed'
        code, out, findings = self.run_main(self.write_fixture(rows))
        self.assertEqual(code, 1)
        self.assertIn('headers do not match', out)
        self.assertNotIn('Validation passed', out)

    def test_published_dataset_passes_in_default_mode(self):
        """The CI step (default mode) passes on the published Extended CSV."""
        code, out, findings = self.run_main(EXTENDED_CSV)
        self.assertEqual(code, 0)
        self.assertIn('[OK] Validation passed', out)
        self.assertTrue(all(level == 'WARNING' for level, _ in findings))


if __name__ == '__main__':
    unittest.main()
