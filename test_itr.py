import unittest
from io import StringIO
from unittest.mock import patch

from itr import calculate_income_from_salary_tax_old, tax_calculation

class TaxCalculationTestCase(unittest.TestCase):
    """
    This test case defines two test methods, test_old_regime_income_from_salary and test_new_regime_income_from_salary, which test the function's behavior when regime is 1 (old regime) and 2 (new regime), respectively.

    Each test method uses the patch context manager from the unittest.mock module to temporarily redirect sys.stdout to a StringIO object, which allows us to capture the function's console output.

    The test methods then call the tax_calculation function with the appropriate arguments, and compare the captured output to the expected output using the assertEqual method.

    Finally, the unittest.main() function is called to run the test case.
    """
    def test_old_regime_income_from_salary(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            tax_calculation(2022, 2023, 1)
        expected_output = "FY 2022 (AY 2023) TAX CALCULATION\n" \
                          "\n1. Income from salary\n" \
                          "\n1.1 Input\n" \
                          "You have selected the old regime\n"
        self.assertEqual(fake_out.getvalue(), expected_output)
    
    def test_new_regime_income_from_salary(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            tax_calculation(2022, 2023, 2)
        expected_output = "FY 2022 (AY 2023) TAX CALCULATION\n" \
                          "\n1. Income from salary\n" \
                          "\n1.1 Input\n" \
                          "You have selected the new regime\n"
        self.assertEqual(fake_out.getvalue(), expected_output)

class CalculateIncomeFromSalaryTaxOldTestCase(unittest.TestCase):
    """
    This test case defines five test methods, which test the function's behavior in various scenarios:

    1. test_no_tax tests the function's behavior when the total income from salary is below the basic exemption limit of Rs. 2,50,000, and expects the tax to be 0.
    2. test_single_slab_tax tests the function's behavior when the total income from salaryis within a single tax slab, and expects the tax to be calculated correctly.
    3. test_multiple_slab_tax tests the function's behavior when the total income from salary is within multiple tax slabs, and expects the tax to be calculated correctly.
    4. test_max_slab_tax tests the function's behavior when the total income from salary is above the highest tax slab, and expects the tax to be calculated correctly.
    5. test_negative_income tests the function's behavior when the total income from salary is negative, and expects an AssertionError to be raised.
    
    Each test method calls the calculate_income_from_salary_tax_old function with a specific input, and compares the returned tax value to the expected value using the assertEqual method. The test_negative_income method uses the assertRaises context manager to check that an AssertionError is raised when the total income from salary is negative.
    
    Finally, the unittest.main() function is called to run the test case.
    """
    def test_no_tax(self):
        self.assertEqual(calculate_income_from_salary_tax_old(200000), 0)
    
    def test_single_slab_tax(self):
        self.assertEqual(calculate_income_from_salary_tax_old(400000), 8580)
    
    def test_multiple_slab_tax(self):
        self.assertEqual(calculate_income_from_salary_tax_old(800000), 82940)
    
    def test_max_slab_tax(self):
        self.assertEqual(calculate_income_from_salary_tax_old(15000000), 4933500)
    
    def test_negative_income(self):
        with self.assertRaises(AssertionError):
            calculate_income_from_salary_tax_old(-10000)
            
if __name__ == '__main__':
    unittest.main()