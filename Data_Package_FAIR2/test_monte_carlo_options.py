import contextlib
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent))

from Python_Code_API_Monte_Carlo import analyze_compound, calculate_new_compound, compare_all_compounds

N = 500  # small iteration count keeps the tests fast


def quiet(func, *args, **kwargs):
    """Call func with its console output suppressed."""
    with contextlib.redirect_stdout(io.StringIO()):
        return func(*args, **kwargs)


class TestMonteCarloOptions(unittest.TestCase):
    """The seed and iteration count requested by the caller must be used."""

    def test_default_seed_is_42(self):
        default = quiet(analyze_compound, 'Rapamycin', n_iterations=N, plot=False)
        seed42 = quiet(analyze_compound, 'Rapamycin', n_iterations=N, plot=False, random_seed=42)
        self.assertEqual(default['CI_lower'], seed42['CI_lower'])
        self.assertEqual(default['CI_upper'], seed42['CI_upper'])

    def test_custom_seed_is_used_and_reproducible(self):
        seed42 = quiet(analyze_compound, 'Rapamycin', n_iterations=N, plot=False, random_seed=42)
        seed7 = quiet(analyze_compound, 'Rapamycin', n_iterations=N, plot=False, random_seed=7)
        seed7_again = quiet(analyze_compound, 'Rapamycin', n_iterations=N, plot=False, random_seed=7)
        self.assertNotEqual(seed42['CI_lower'], seed7['CI_lower'])
        self.assertEqual(seed7['CI_lower'], seed7_again['CI_lower'])

    def test_iterations_are_used(self):
        result = quiet(analyze_compound, 'Rapamycin', n_iterations=N, plot=False)
        self.assertEqual(len(result['samples']), N)

    def test_new_compound_uses_seed(self):
        params = dict(K_d=0.1, tau=120, t_onset=1440, EC50=1, n_iterations=N)
        seed42 = quiet(calculate_new_compound, **params)
        seed7 = quiet(calculate_new_compound, random_seed=7, **params)
        self.assertEqual(len(seed42['all_samples']), N)
        self.assertNotEqual(seed42['CI_lower'], seed7['CI_lower'])

    def test_compare_all_compounds_passes_options(self):
        cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)  # compare_all_compounds writes its CSV to the working directory
            try:
                summary = quiet(compare_all_compounds, plot_comparison=False,
                                n_iterations=N, random_seed=7)
            finally:
                os.chdir(cwd)
        expected = quiet(analyze_compound, 'Rapamycin', n_iterations=N, plot=False, random_seed=7)
        row = summary[summary['Compound'] == 'Rapamycin'].iloc[0]
        self.assertEqual(row['API'], expected['API_relative_median'])
        self.assertEqual(row['CI_Lower'], expected['CI_lower'])


if __name__ == '__main__':
    unittest.main()
