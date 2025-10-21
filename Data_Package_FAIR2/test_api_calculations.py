import unittest
from Python_Code_API_Monte_Carlo import calculate_API_absolute, calculate_API_relative, assign_confidence_grade

class TestAPICalculations(unittest.TestCase):
    """Unit tests for the API calculation script."""

    def test_salvinorin_a_api(self):
        """Test API calculation with known values for Salvinorin A."""
        api_abs = calculate_API_absolute(K_d_nM=1.8, tau_residence_min=25,
                                         t_onset_min=1, EC50_nM=2)
        # The expected value is (1/1.8 * 25) / (1 * 2) = 6.9444...
        self.assertAlmostEqual(api_abs, 6.9444, places=4)

        # The reference API is ~6.9444
        api_rel = calculate_API_relative(api_abs, reference_API=6.94444444)
        self.assertAlmostEqual(api_rel, 1.00, places=2)

    def test_rapamycin_api(self):
        """Test API calculation with known values for Rapamycin."""
        # K_d=0.1, tau=120, t_onset=1440, EC50=1
        api_abs = calculate_API_absolute(K_d_nM=0.1, tau_residence_min=120,
                                         t_onset_min=1440, EC50_nM=1)
        # (1/0.1 * 120) / (1440 * 1) = 1200 / 1440 = 0.8333...
        self.assertAlmostEqual(api_abs, 0.8333, places=4)
        
        # Relative to Salvinorin A's absolute API
        api_rel = calculate_API_relative(api_abs, reference_API=6.94444444)
        self.assertAlmostEqual(api_rel, 0.120, places=3)
        
    def test_invalid_inputs(self):
        """Test that the function raises ValueError for non-positive inputs."""
        with self.assertRaises(ValueError):
            calculate_API_absolute(0, 10, 10, 10)
        with self.assertRaises(ValueError):
            calculate_API_absolute(10, -5, 10, 10)
        with self.assertRaises(ValueError):
            calculate_API_absolute(10, 10, 0, 10)
        with self.assertRaises(ValueError):
            calculate_API_absolute(10, 10, 10, -1)

    def test_confidence_grading(self):
        """Test the confidence grading logic."""
        # Score 12 -> VERY HIGH
        self.assertEqual(assign_confidence_grade('measured', 'measured', 'measured', 'measured'), 'VERY HIGH')
        # Score 3*3 + 2 = 11 -> VERY HIGH
        self.assertEqual(assign_confidence_grade('measured', 'measured', 'measured', 'estimated'), 'VERY HIGH')
        # Score 3*2 + 2*2 = 10 -> HIGH
        self.assertEqual(assign_confidence_grade('measured', 'measured', 'estimated', 'estimated'), 'HIGH')
        # Score 3 + 2*3 = 9 -> HIGH
        self.assertEqual(assign_confidence_grade('measured', 'estimated', 'estimated', 'estimated'), 'HIGH')
        # Score 2*4 = 8 -> MODERATE
        self.assertEqual(assign_confidence_grade('estimated', 'estimated', 'estimated', 'estimated'), 'MODERATE')
        # Score 3+2+2+1 = 8 -> MODERATE
        self.assertEqual(assign_confidence_grade('measured', 'estimated', 'estimated', 'inferred'), 'MODERATE')
        # Score 2*2+1*2 = 6 -> MODERATE
        self.assertEqual(assign_confidence_grade('estimated', 'estimated', 'inferred', 'inferred'), 'MODERATE')
        # Score 3+1*3 = 6 -> MODERATE
        self.assertEqual(assign_confidence_grade('measured', 'inferred', 'inferred', 'inferred'), 'MODERATE')
        # Score 2+1*3 = 5 -> LOW
        self.assertEqual(assign_confidence_grade('estimated', 'inferred', 'inferred', 'inferred'), 'LOW')
        # Score 1*4 = 4 -> LOW
        self.assertEqual(assign_confidence_grade('inferred', 'inferred', 'inferred', 'inferred'), 'LOW')


if __name__ == '__main__':
    unittest.main()
