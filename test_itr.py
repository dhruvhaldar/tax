import unittest
from io import StringIO
from unittest.mock import patch

from itr import calculate_income_from_salary_tax_new, calculate_income_from_salary_tax_old, tax_calculation


class TestTaxCalculation(unittest.TestCase):
    
    def test_tax_calculation(self):
        fy_year = "2022-23"
        ay_year = "2023-24"
        regime = 1
        expected_output = "FY 2022-23 (AY 2023-24) TAX CALCULATION\n\n1. Income from salary\n\n1.1 Input\nYou have selected the old regime\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            tax_calculation(fy_year, ay_year, regime)
            self.assertEqual(fake_out.getvalue(), expected_output)

class TestCalculateIncomeFromSalaryTaxOld(unittest.TestCase):
    
    def test_calculate_income_from_salary_tax_old(self):
        total_income_from_salary = 500000
        expected_output = 14300.0
        self.assertAlmostEqual(calculate_income_from_salary_tax_old(total_income_from_salary), expected_output)
        
    def test_calculate_income_from_salary_tax_slab1(self):
        total_income_from_salary = 150000
        expected_output = 0
        self.assertAlmostEqual(calculate_income_from_salary_tax_old(total_income_from_salary), expected_output)
        
    def test_calculate_income_from_salary_tax_slab2(self):
        total_income_from_salary = 3500000
        expected_output = 986700
        self.assertAlmostEqual(calculate_income_from_salary_tax_old(total_income_from_salary), expected_output)

class TestCalculateIncomeFromSalaryTaxNew(unittest.TestCase):

    # def test_tax_below_slab_one(self):
    #     self.assertEqual(calculate_income_from_salary_tax_new(200000), 0)
    
    # def test_tax_in_slab_one(self):
    #     self.assertEqual(calculate_income_from_salary_tax_new(300000), 2500)
    
    # def test_tax_in_slab_two(self):
    #     self.assertEqual(calculate_income_from_salary_tax_new(600000), 45000)
    
    # def test_tax_in_slab_three(self):
    #     self.assertEqual(calculate_income_from_salary_tax_new(800000), 105000)
    
    # def test_tax_in_slab_four(self):
    #     self.assertEqual(calculate_income_from_salary_tax_new(1200000), 225000)
    
    # def test_tax_in_slab_five(self):
    #     self.assertEqual(calculate_income_from_salary_tax_new(1400000), 325000)
    
    # def test_tax_above_slab_six(self):
    #     self.assertEqual(calculate_income_from_salary_tax_new(2000000), 525000)
    
    # def test_tax_with_surcharge(self):
    #     self.assertEqual(calculate_income_from_salary_tax_new(10000000), 2966250)


    if __name__ == '__main__':
        unittest.main()