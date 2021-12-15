#LINK PROBLEM: https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-6-sum-square-difference

"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.
"""

import numpy as np

def sumSquareDifference(n):
  resultado  = (np.arange(1, n+1).sum())**2 - ((np.arange(1, n+1)**2).sum())
  return resultado


if __name__ == '__main__':


    #should return a number.
    sumSquareDifference(2)

    # should return 2640.
    print(sumSquareDifference(10))

    # should return 41230.
    print(sumSquareDifference(20))

    # should return 25164150.
    print(sumSquareDifference(100))
