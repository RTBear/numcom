# Number of Combinations Calculator

## Problem Statement
This project calculates all unique permutations of M digits (1-9) which combined using M-1 basic mathmatical operations equal the number N. Allowed
operators include:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)

### Definitions and Considerations
For the purposes of this project, the following terms are defined as follows.
  - permutations: each digit and each operator may be used at most once
  - unique: solutions where all the digits are the same and in the same order,
  only count once, regardless of operators used. 
  - order of operations: strict order of operations is applied. In other words,
  this solution does not account for the usage of parenthesis.

## Solutions
The general form of solutions would look like:
```
  Digit_0 Operator_0 Digit_1 Operator_1 Digit_2 ... Operator_(M-1) Digit_M
```

One example solution to the problem where M = 4 and N = 24 is provided below:
```
  9 * 2 + 7 - 1 = 24
```

## Running
Run the combination calculator by running the `main.py` file. e.g.

```
python3 app/main.py
```

## Testing
Run the test suite by running the following in your terminal:

```
python3 -m unittest discover test
```