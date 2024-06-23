''' Calculates Number of Combinations.

This class handles the actual solving of the problem statement outlined
in the readme. This class calculates all unique permutations of M digits (1-9)
which combined using M-1 basic mathmatical operations equal the number N.

See README.md for more info and the problem statement.
'''

import logging, itertools, operator
from calculator import Calculator
logger = logging.getLogger(__name__) #does this define this in main.py too?

class NumCom:
  OPERATORS = [operator.add, operator.sub, operator.mul, operator.truediv]
  DIGITS = list(range(1,10))
  # DIGITS = list(range(1,3))
  DIGIT_COUNT = 4
  OPERATOR_COUNT = 3
  DESIRED_RESULT = 24

  # def __init__(self):
  #   self.desired_result = desired_result

  def compose_rpn_stack(self,digits,operators):
    digits = list(digits)
    operators = list(operators)
    rpn_stack = [digits.pop(0),digits.pop(0),operators.pop(0)]

    #zip produces a list of tuples, we want a flat list, and chain flattens it
    rpn_stack_tail = list(itertools.chain.from_iterable(zip(digits,operators)))

    rpn_stack.extend(rpn_stack_tail)
    return rpn_stack
  
  def generate_digit_list(self):
    #generate list of all permutations of 4 digits
    self.DIGIT_LIST = list(itertools.permutations(self.DIGITS,4))

  def generate_operator_list(self):
    #generate list of all permutations of 3 operators
    self.OPERATOR_LIST = list(itertools.permutations(self.OPERATORS,3))

  def run(self):
    self.generate_digit_list()
    self.generate_operator_list()

    results = []

    for digits in self.DIGIT_LIST:
      for operators in self.OPERATOR_LIST:
        candidate = self.compose_rpn_stack(digits,operators)
        calculator = Calculator()
        calculator.push(candidate)
        result = calculator.calculate()
        logger.debug(f'got {result} from {candidate}')
        if result == self.DESIRED_RESULT:
          results.append(digits)
    return results
  

if __name__ == '__main__':
  logging.basicConfig(filename='debug.log', level=logging.DEBUG)
  numcom = NumCom()
  results = numcom.run()
  result_set = set()
  for result in results:
    val = tuple(sorted(result))
    result_set.add(val)
  print(len(results))
  for val in result_set:
    print(val)
  print(len(result_set))
