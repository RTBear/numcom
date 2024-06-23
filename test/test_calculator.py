import unittest
import context
import operator, logging
from app.calculator import Calculator

class TestPush(unittest.TestCase):

    def test_push_array(self):
        calculator = Calculator()
        calculator.push([1,2,operator.add])
        self.assertEqual(calculator.stack, [1,2,operator.add], 'The stack is wrong.')

    def test_push_int(self):
        calculator = Calculator()
        calculator.push(1)
        calculator.push(2)
        self.assertEqual(calculator.stack, [1,2], 'The stack is wrong.')
    
    def test_push_operator(self):
        calculator = Calculator()
        calculator.push(operator.add)
        calculator.push(operator.sub)
        self.assertEqual(calculator.stack, [operator.add,operator.sub], 'The stack is wrong.')

class TestCalculate(unittest.TestCase):
    def test_calculate_valid_stack_1(self):
        calculator = Calculator()
        calculator.push([1,2,operator.add])
        self.assertEqual(calculator.calculate(), 3, 'incorrect result')

    def test_calculate_valid_stack_2(self):
        calculator = Calculator()
        calculator.push([1,2,operator.add,3,operator.add])
        self.assertEqual(calculator.calculate(), 6, 'incorrect result')

    def test_calculate_multiple_push_valid_stack(self):
        calculator = Calculator()
        calculator.push([1,2,operator.add])
        self.assertEqual(calculator.calculate(), 3, 'incorrect result')
        calculator.push([3,operator.sub])
        self.assertEqual(calculator.calculate(), 0, 'incorrect result')

    def test_calculate_push_invalid_stack(self):
        calculator = Calculator()
        calculator.push([1,2,operator.add,3,operator.sub,4])
        self.assertRaises(ValueError, calculator.calculate)

    def test_calculate_multiple_push_invalid_stack(self):
        calculator = Calculator()
        calculator.push([1,2,operator.add])
        self.assertEqual(calculator.calculate(), 3, 'incorrect result')
        calculator.push([3,operator.sub,4])
        self.assertRaises(ValueError, calculator.calculate)
    
    def test_calculate_invalid_stack_only_operands(self):
        calculator = Calculator()
        calculator.push([1,2])
        with self.assertRaises(ValueError) as context:
            calculator.calculate()
        self.assertTrue('Invalid stack -- got operand when expected operator' in str(context.exception))

    def test_calculate_invalid_stack_only_operands2(self):
        calculator = Calculator()
        calculator.push([1,2,3,4,5])
        with self.assertRaises(ValueError) as context:
            calculator.calculate()
        self.assertTrue('Invalid stack -- got operand when expected operator' in str(context.exception))

    def test_complicated_stack(self):
        calculator = Calculator()
        calculator.push([1,2,3,operator.add,operator.sub])
        self.assertEqual(calculator.calculate(), -4, 'incorrect result')

    def test_calculate_too_many_operands(self):
        calculator = Calculator()
        calculator.push([1,2,1,operator.add])
        with self.assertRaises(ValueError) as context:
            calculator.calculate()
        self.assertTrue('Invalid stack -- Too many operands in a row' in str(context.exception))

    def test_calculate_too_many_operands2(self):
        calculator = Calculator()
        calculator.push([operator.add,2,1,operator.add])
        with self.assertRaises(ValueError) as context:
            calculator.calculate()
        self.assertTrue('Invalid stack -- Too many operands in a row' in str(context.exception))

    def test_calculate_too_many_operands3(self):
        calculator = Calculator()
        calculator.push([1,operator.add,2,1,operator.add])
        with self.assertRaises(ValueError) as context:
            calculator.calculate()
        self.assertTrue('Invalid stack -- Too many operands in a row' in str(context.exception))

    def test_calculate_too_many_operands4(self):
        calculator = Calculator()
        calculator.push([1,operator.add])
        with self.assertRaises(ValueError) as context:
            calculator.calculate()
        self.assertTrue('Invalid Stack -- Too few operands' in str(context.exception))

    def test_all_operators(self):
        calculator = Calculator()
        calculator.push([operator.add,operator.add,operator.add])
        with self.assertRaises(ValueError) as context:
            calculator.calculate()
        self.assertTrue('Invalid Stack -- Too few operands' in str(context.exception))

    def test_too_few_operands(self):
        calculator = Calculator()
        calculator.push([1,2,operator.add,operator.add,operator.add])
        with self.assertRaises(ValueError) as context:
            calculator.calculate()
        self.assertTrue('Invalid Stack -- Too few operands' in str(context.exception))

    def test_numcom_calculation(self):
        calculator = Calculator()
        calculator.push([9,2,operator.mul,7,operator.add,1,operator.sub])
        self.assertEqual(calculator.calculate(), 24, 'incorrect result')

    def test_numcom_calculation2(self):
        calculator = Calculator()
        calculator.push([9,2,operator.mul,7,operator.add,1,operator.sub])
        self.assertEqual(calculator.calculate(), 24, 'incorrect result')

if __name__ == '__main__':
    logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    unittest.main()
