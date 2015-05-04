import unittest
from calculator import Calculator

class TestCalculatorMethods(unittest.TestCase):

    calc_test = Calculator()

    #Starter unit test
    def test_calculator(self):
        self.assertTrue("S".__eq__(self.calc_test.calculator("S")))




#Keep this method to execute all your tests cases through the cmdLine
if __name__ == '__main__':
    unittest.main()


