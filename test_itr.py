import unittest

from itr import income_from_hp, tax_calculation

class TestTaxCalculation(unittest.TestCase):
    def test_tax_calculation(self):
        self.assertEqual(tax_calculation(2022, 2023, 350000, 1), None)
        self.assertEqual(tax_calculation(2022, 2023, 1000, 2), None)
        self.assertEqual(tax_calculation(2022, 2023, 8000000, 2), None)

class TestIncomeFromHP(unittest.TestCase):
  def test_self_occupied(self):
    self.assertEqual(income_from_hp("self-occupied", 150000), -150000)
    self.assertEqual(income_from_hp("self-occupied", 250000), -200000)
  
  def test_let_out(self):
    self.assertEqual(income_from_hp("let out", 0), 42000.0)
    self.assertEqual(income_from_hp("let out", 50000), -8000.0)
  
  def test_deemed_let_out(self):
    self.assertEqual(income_from_hp("deemed let out", 0), 70000.0)
    self.assertEqual(income_from_hp("deemed let out", 50000), 20000.0)
  
  def test_invalid_input(self):
    with self.assertRaises(ValueError):
      income_from_hp("invalid", 0)
      
if __name__ == '__main__':
    unittest.main()