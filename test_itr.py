import unittest
from io import StringIO
from unittest.mock import patch

from itr import tax_calculation

class TaxCalculationTestCase(unittest.TestCase):
    
    def test_old_regime_income_from_salary(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            tax_calculation(2022, 2023, 1)
        # expected_output = "FY 2022 (AY 2023) TAX CALCULATION\n" \
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

if __name__ == '__main__':
    unittest.main()