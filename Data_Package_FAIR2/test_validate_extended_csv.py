import contextlib
import csv
import io
import sys
import tempfile
import unittest
from pathlib import Path

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent))

from validate_extended_csv import main

DATA_DIR = Path(__file__).parent
EXTENDED_CSV = DATA_DIR / 'Compound_Properties_Experimental_Extended.csv'
MAIN_CSV = DATA_DIR / 'Compound_Properties_Database.csv'


class TestValidateExtendedCSV(unittest.TestCase):
    """Regression tests for validate_extended_csv.py, using corrupted copies
    of the Extended CSV written to a temporary directory."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp_dir = Path(tmp.name)

    def run_main(self, extended_csv):
        """Run the validator and return (exit code, printed output)."""
        out = io.StringIO()
        code = 0
        with contextlib.redirect_stdout(out):
            try:
                main(extended_csv, MAIN_CSV)
            except SystemExit as e:
                code = e.code
        return code, out.getvalue()

    def read_rows(self):
        with open(EXTENDED_CSV, newline='', encoding='utf-8') as f:
            return list(csv.reader(f))

    def write_fixture(self, rows):
        path = self.tmp_dir / 'extended_corrupted.csv'
        with open(path, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerows(rows)
        return path

    def test_unmodified_dataset_passes(self):
        """The published Extended CSV passes validation."""
        code, out = self.run_main(EXTENDED_CSV)
        self.assertEqual(code, 0)
        self.assertIn('[OK] Validation passed', out)

    def test_lowercase_placeholder_fails(self):
        """A lowercase placeholder fails without reporting success."""
        rows = self.read_rows()
        row, col = next((r, c) for r in range(1, len(rows))
                        for c, val in enumerate(rows[r]) if val == 'NR')
        rows[row][col] = 'nr'
        code, out = self.run_main(self.write_fixture(rows))
        self.assertEqual(code, 1)
        self.assertIn('Invalid placeholder case "nr"', out)
        self.assertNotIn('Validation passed', out)

    def test_header_mismatch_fails(self):
        """A header that differs from the main database fails."""
        rows = self.read_rows()
        rows[0][-1] += '_renamed'
        code, out = self.run_main(self.write_fixture(rows))
        self.assertEqual(code, 1)
        self.assertIn('headers do not match', out)
        self.assertNotIn('Validation passed', out)


if __name__ == '__main__':
    unittest.main()
