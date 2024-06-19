''' Calculates Number of Combinations.

This class handles the actual solving of the problem statement outlined
in the readme. This class calculates all unique permutations of M digits (1-9)
which combined using M-1 basic mathmatical operations equal the number N.

See README.md for more info and the problem statement.
'''

import logging
logger = logging.getLogger(__name__) #does this define this in main.py too?

class NumCom:
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
