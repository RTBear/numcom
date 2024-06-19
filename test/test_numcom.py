import unittest
import context
from app.numcom import NumCom

class TestNumCom(unittest.TestCase):

    def test_push_array(self):
        numcom = NumCom()
        numcom.push([1,2,'+'])
        self.assertEqual(numcom.stack, [1,2,'+'], 'The stack is wrong.')

    def test_push_int(self):
        numcom = NumCom()
        numcom.push(1)
        numcom.push(2)
        self.assertEqual(numcom.stack, [1,2], 'The stack is wrong.')
    
    def test_push_operator(self):
        numcom = NumCom()
        numcom.push('+')
        numcom.push('-')
        self.assertEqual(numcom.stack, ['+','-'], 'The stack is wrong.')

if __name__ == '__main__':
    unittest.main()
