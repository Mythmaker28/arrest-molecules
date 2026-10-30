import contextlib
import csv
import io
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent))

from data_validation import validate_compound_database, validate_predictions_matrix

DATA_DIR = Path(__file__).parent
CORE_CSV = DATA_DIR / 'Compound_Properties_Database.csv'
MATRIX_CSV = DATA_DIR / 'Confidence_Grading_Matrix.csv'

REQUIRED_COLUMNS = ['Compound_Name', 'K_d_nM', 'EC50_nM', 'tau_residence_min', 'k_off_per_min',
                    'K_i_Source_PMID']
POSITIVE_COLUMNS = ['K_d_nM', 'EC50_nM', 'tau_residence_min', 'k_off_per_min']


def run(validator, path):
    """Call a validator with its console output captured; return (result, output)."""
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        result = validator(str(path))
    return result, out.getvalue()


class TestDataValidation(unittest.TestCase):
    """data_validation.py on the published files and on corrupted copies of them."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp_dir = Path(tmp.name)

    def corrupted_copy(self, source, column, value, row=1):
        """Copy source with one cell replaced (row 0 is the header) and return the copy's path."""
        with open(source, newline='', encoding='utf-8') as f:
            rows = [r for r in csv.reader(f) if r]
        rows[row][rows[0].index(column)] = value
        path = self.tmp_dir / source.name
        with open(path, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerows(rows)
        return path

    def test_unmodified_core_dataset_passes(self):
        result, out = run(validate_compound_database, CORE_CSV)
        self.assertTrue(result)
        self.assertNotIn('[AVERTISSEMENT]', out)

    def test_unmodified_predictions_matrix_passes(self):
        result, _ = run(validate_predictions_matrix, MATRIX_CSV)
        self.assertTrue(result)

    def test_missing_file_fails(self):
        for validator in (validate_compound_database, validate_predictions_matrix):
            with self.subTest(validator=validator.__name__):
                result, out = run(validator, self.tmp_dir / 'missing.csv')
                self.assertFalse(result)
                self.assertIn('[ERREUR]', out)

    def test_missing_required_column_fails(self):
        for column in REQUIRED_COLUMNS:
            with self.subTest(column=column):
                path = self.corrupted_copy(CORE_CSV, column, column + '_renamed', row=0)
                result, out = run(validate_compound_database, path)
                self.assertFalse(result)
                self.assertIn('Colonnes manquantes', out)

    def test_non_positive_value_fails(self):
        for column in POSITIVE_COLUMNS:
            for value in ('0', '-1'):
                with self.subTest(column=column, value=value):
                    result, out = run(validate_compound_database,
                                      self.corrupted_copy(CORE_CSV, column, value))
                    self.assertFalse(result)
                    self.assertIn(f'{column}: 1 valeurs', out)

    def test_invalid_confidence_level_fails(self):
        for value in ('high', 'Unknown', ''):
            with self.subTest(value=value):
                result, out = run(validate_predictions_matrix,
                                  self.corrupted_copy(MATRIX_CSV, 'Confidence_Level', value))
                self.assertFalse(result)
                self.assertIn('1 niveaux de confiance invalides', out)

    # The three checks below only print a warning; whether they should fail
    # validation is left open (ROADMAP milestone 2), so the tests only check
    # that the problem is reported.

    def test_tau_inconsistent_with_k_off_is_reported(self):
        _, out = run(validate_compound_database,
                     self.corrupted_copy(CORE_CSV, 'tau_residence_min', '50'))
        self.assertIn('[AVERTISSEMENT] 1 incoherences tau = 1/k_off', out)
        self.assertIn('Salvinorin A', out)

    def test_non_numeric_pmid_is_reported(self):
        _, out = run(validate_compound_database,
                     self.corrupted_copy(CORE_CSV, 'K_i_Source_PMID', 'not-a-pmid'))
        self.assertIn('[AVERTISSEMENT] 1 PMIDs invalides', out)
        self.assertIn('Salvinorin A: not-a-pmid', out)

    def test_missing_critical_value_is_reported(self):
        _, out = run(validate_compound_database, self.corrupted_copy(CORE_CSV, 'K_d_nM', ''))
        self.assertIn('Valeurs manquantes dans colonnes critiques', out)
        self.assertIn('K_d_nM: 1 valeurs manquantes', out)

    def test_command_exits_with_error_on_invalid_data(self):
        self.corrupted_copy(CORE_CSV, 'K_d_nM', '0')
        shutil.copy(MATRIX_CSV, self.tmp_dir)
        completed = subprocess.run([sys.executable, str(DATA_DIR / 'data_validation.py')],
                                   cwd=self.tmp_dir, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   env=dict(os.environ, PYTHONIOENCODING='utf-8'))
        self.assertEqual(completed.returncode, 1)
        self.assertIn('[ÉCHEC] Certaines validations ont échoué', completed.stdout.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
