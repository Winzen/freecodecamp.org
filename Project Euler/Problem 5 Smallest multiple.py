#LINK PROBLEM: https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-5-smallest-multiple

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?
"""

import numpy as np

def smallestMult(n):

  return np.lcm.reduce(np.arange(1, n+1))


if __name__ == '__main__':
    #should return a number.
    print(smallestMult(2))

    #should return 60.
    print(smallestMult(5))

    # should return 420.
    print(smallestMult(7))

    # should return 2520.
    print(smallestMult(10))