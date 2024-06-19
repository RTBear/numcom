''' Reverse Polish Notation Calculator.

I make no claims this is an optimal implementation, but hopefully it is at least
functional. ;) In reverse Polish notation, the operators follow their operands.
For example, to add 3 and 4 together, the expression is 3 4 + rather than 3 + 4.
The conventional notation expression 3 − 4 + 5 becomes 3 4 − 5 + in reverse 
Polish notation: 4 is first subtracted from 3, then 5 is added to it.

Supported operators include: +,-,*,/
'''

import logging
logger = logging.getLogger(__name__) #does this define this in main.py too?

class Calculator:
  def __init__(self):
    self.stack = []

  # add items to the stack
  def push(self, items):
    logger.debug(f'pushing to the stack: {items}')
    if hasattr(items, '__iter__'):
      self.stack.extend(items)
    else:
      self.stack.append(items)

  # process the current stack
  def calculate(self):
    logger.debug(f'caluclating stack of: {self.stack}')
    return 0
