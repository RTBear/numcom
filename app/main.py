#!/usr/bin/python3

''' Entry point to the program. Orchestrates all the fun.
'''

from calculator import Calculator
import logging
logger = logging.getLogger(__name__)

def main():
  c = Calculator()
  c.push([1,3,'+'])
  c.calculate()

if __name__ == '__main__':
  logging.basicConfig(filename='debug.log', level=logging.DEBUG)
  logger.info('--------- STARTING ---------')
  main()
