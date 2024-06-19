import unittest
import context
from app.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_push_array(self):
        calculator = Calculator()
        calculator.push([1,2,'+'])
        self.assertEqual(calculator.stack, [1,2,'+'], 'The stack is wrong.')

    def test_push_int(self):
        calculator = Calculator()
        calculator.push(1)
        calculator.push(2)
        self.assertEqual(calculator.stack, [1,2], 'The stack is wrong.')
    
    def test_push_operator(self):
        calculator = Calculator()
        calculator.push('+')
        calculator.push('-')
        self.assertEqual(calculator.stack, ['+','-'], 'The stack is wrong.')

if __name__ == '__main__':
    unittest.main()
