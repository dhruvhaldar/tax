import sys
import unittest

from itr import calculate_income_tax_new, calculate_income_tax_old

class TestCalculateIncomeTaxOld(unittest.TestCase):

    def test_total_income_under_limit(self):
        self.assertEqual(calculate_income_tax_old(10000), 0)
        self.assertEqual(calculate_income_tax_new(10000), 0)

    def test_total_income_in_5_percent_slab(self):
        self.assertEqual(calculate_income_tax_old(260000), 500)
        self.assertEqual(calculate_income_tax_new(260000), 500)

    def test_total_income_in_20_percent_slab(self):
        self.assertEqual(calculate_income_tax_old(600000), 55000)
        self.assertEqual(calculate_income_tax_new(600000), 55000)


    def test_total_income_in_30_percent_slab(self):
        self.assertEqual(calculate_income_tax_old(1000000), 170000)
        self.assertEqual(calculate_income_tax_new(1000000), 170000)

    def test_total_income_above_30_percent_slab(self):
        self.assertEqual(calculate_income_tax_old(2000000), 470000)
        self.assertEqual(calculate_income_tax_new(2000000), 470000)

if __name__ == '__main__':
    regime = sys.argv[1] if len(sys.argv) > 1 else 'Old'

    if regime.lower() == 'old':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculateIncomeTaxOld)
    elif regime.lower() == 'new':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculateIncomeTaxNew)
    else:
        print("Invalid regime specified")
        sys.exit(1)

    unittest.TextTestRunner().run(suite)