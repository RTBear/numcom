# Number of Combinations Calculator

## Problem Statement
This project calculates all unique permutations of 4 digits (1-9) which combined
using 3 of the following basic mathmatical operations equal the number 24:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)

In the future, I may extend this to be M digits equalling any number N.

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
  Digit_0 Oper_0 Digit_1 Oper_1 Digit_2 Oper_2 Digit_3
```

One example solution to the problem is provided below:
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