#LINK PROBLEM: https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-1-multiples-of-3-and-5

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
"""
import numpy as np

def multiplesOf3and5(number):
    sequencia = np.arange(1, number+1)
    sequencia = sequencia[(sequencia % 3 == 0) | (sequencia % 5 == 0)].sum(dtype=int)
    return sequencia

if __name__ == '__main__':
    """should return a number."""
    print(multiplesOf3and5(10))

    """should return 543."""
    print(multiplesOf3and5(49))

    """should return 233168."""
    print(multiplesOf3and5(1000))

    """should return 16687353."""
    print(multiplesOf3and5(8456))

    """should return 89301183."""
    print(multiplesOf3and5(19564))
