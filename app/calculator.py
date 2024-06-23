''' Reverse Polish Notation Calculator.

I make no claims this is an optimal implementation, but hopefully it is at least
functional. ;) In reverse Polish notation, the operators follow their operands.
For example, to add 3 and 4 together, the expression is 3 4 + rather than 3 + 4.
The conventional notation expression 3 − 4 + 5 becomes 3 4 − 5 + in reverse 
Polish notation: 4 is first subtracted from 3, then 5 is added to it.

Supported operators include: +,-,*,/
'''

import logging, operator
logger = logging.getLogger(__name__) #does this define this in main.py too?

class Calculator:
  def __init__(self):
    self.stack = []
    self.current_value = None
    logger.info("hi, I'm a new Calculator -----------------------------------")

  # add items to the stack
  def push(self, items):
    logger.debug(f'pushing to the stack: {items}')
    if hasattr(items, '__iter__'):
      self.stack.extend(items)
    else:
      self.stack.append(items)

  ''' recursively evaluate operators
  for example:
  
  1,2,3,+,-

  evaluates as

  -
    +
      1,2,3
    1,5
  -4
  '''
  def evaluate(self, operation):
    logger.debug(f'evaluating {operation} with stack of: {self.stack}')

    if len(self.stack) > 0:
      right = self.stack.pop()
    else:
      raise ValueError("Invalid Stack -- Too few operands")
    
    # check for another operator and call it recursively
    if callable(right):
      right = self.evaluate(right)

    if len(self.stack) > 0:
      left = self.stack.pop()
    else:
      # You hit the end of the stack, grab the current_value as `left` if present
      # this allows for multiple calls to `.calculate()` on the same instance
      if self.current_value is None:
        raise ValueError("Invalid Stack -- Too few operands")
      else:
        left = self.current_value

    if callable(left):
      left = self.evaluate(left)

    #base case
    return operation(left,right)

  # process the current stack
  def calculate(self):
    operation = self.stack.pop()
    
    if not callable(operation):
      raise ValueError("Invalid stack -- got operand when expected operator")
    
    self.current_value = self.evaluate(operation)

    # if there is anything left on the stack, then the stack was bad
    if len(self.stack) != 0:
      raise ValueError("Invalid stack -- Too many operands in a row")
      
    return self.current_value
