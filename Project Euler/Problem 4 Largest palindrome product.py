#LINK PROBLEM:https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-4-largest-palindrome-product

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two n-digit numbers.
"""

import numpy as np
def largestPalindromeProduct(n):
  n = int('9'*n)
  palindros = np.append([], [])

  while n >= (n*0.9):
    max = np.arange(1, n+1, dtype=int)*n
    reverse = np.array(list(map(lambda x: str(x)[::-1], max)), dtype=int)
    max = max[max == reverse]
    palindros = np.append(palindros, max)
    n -= 1

  return palindros.astype(int).max()

if __name__ == '__main__':
    #should return a number.
    largestPalindromeProduct(2)
    # should return 9009..
    print(largestPalindromeProduct(2))
    # should return 906609.
    print(largestPalindromeProduct(3))
