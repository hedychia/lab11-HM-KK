# https://github.com/hedychia/lab11-HM-KK.git
# Partner 1: Haiden Machado
# Partner 2: Kai Kim



import unittest
from calculator import *
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-2, 2), 0)
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(3, 8), -5)##

    ####Partner 1
    def test_multiply(self): # 3 assertions
       self.assertEqual(calculator.mul(12, 2), 24)
       self.assertEqual(calculator.mul(5, 0), 0)
       self.assertAlmostEqual(calculator.mul(3.3, 3), 9.9)

    def test_divide(self): # 3 assertions
       self.assertAlmostEqual(calculator.div(7,2), 3.5)
       self.assertEqual(calculator.div(10,2), 5)
       self.assertEqual(calculator.div(0, 100), 0)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 27), 3)
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 5)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
     with self.assertRaises(ValueError):
        logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
       self.assertEqual(hypotenuse(3,4), 5)
       self.assertAlmostEqual(hypotenuse(1,1), math.sqrt(2))
       self.assertAlmostEqual(hypotenuse(5, 12), 13)
  

    def test_sqrt(self): # 3 assertions
    
     with self.assertRaises(ValueError):
      square_root(-3)
      self.assertEqual(square_root(25),5)
      self.assertAlmostEqual(square_root(3), math.sqrt(3))

    
# Do not touch this
if __name__ == "__main__":
    unittest.main()