import unittest

from itr import tax_calculation

class TestTaxCalculation(unittest.TestCase):
    def test_tax_calculation(self):
        self.assertEqual(tax_calculation(2022, 2023, 350000, 1), None)
        self.assertEqual(tax_calculation(2022, 2023, 1000, 2), None)
        self.assertEqual(tax_calculation(2022, 2023, 8000000, 2), None)

if __name__ == '__main__':
    unittest.main()