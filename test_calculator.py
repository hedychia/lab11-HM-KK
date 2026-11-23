import unittest
from calculator import *
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####Partner 1
    def test_multiply(self): # 3 assertions
       self.assertEqual(calculator.multiply(12, 2), 24)
       self.assertEqual(calculator.multiply(5, 0), 0)
       self.assertAlmostEqual(calculator.multiply(3.3, 3), 9.9)

    def test_divide(self): # 3 assertions
       self.assertAlmostEqual(calculator.divide(7,2), 2.5)
       self.assertEqual(calculator.divide(10,2), 5)
       self.assertEqual(calculator.divide(0, 100), 0)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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