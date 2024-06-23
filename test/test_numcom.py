import unittest
import context
import operator, logging
from app.numcom import NumCom

class TestRun(unittest.TestCase):

    def test_run(self):
        numcom = NumCom()
        self.assertEqual(numcom.run(), 4, 'output is wrong.')

class TestComposeRpnStack(unittest.TestCase):
    def test1(self):
        numcom = NumCom()
        digits = [9,2,7,1]
        operators = [operator.mul,operator.add,operator.sub]
        self.assertEqual(numcom.compose_rpn_stack(digits,operators), [9,2,operator.mul,7,operator.add,1,operator.sub])

class TestGenerateDigitList(unittest.TestCase):
    def test_correct_list_length(self):
        numcom = NumCom()
        numcom.generate_digit_list()
        self.assertEqual(len(numcom.DIGIT_LIST), 3024)

class TestGenerateOperatorList(unittest.TestCase):
    def test_correct_list_length(self):
        numcom = NumCom()
        numcom.generate_operator_list()
        self.assertEqual(len(numcom.OPERATOR_LIST), 24)
        
if __name__ == '__main__':
    logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    unittest.main()
