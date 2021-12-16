#LINK PROBLEM:https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-7-10001st-prime

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the nth prime number?
"""

import numpy as np

def nthPrime(n):
  primos = [2]
  memorie = np.array(2)
  x = 3

  while len(primos) <= n:
    if len((memorie[x % memorie == 0])) == 0:
      primos.append(x)
    memorie = np.append(memorie, x)
    x+=1

  return primos[n-1]


if __name__ == '__main__':

    #should return a number.
    nthPrime(6)

    #should return 13.
    print(nthPrime(6))

    # should return 29.
    print(nthPrime(10))

    # should return 541.
    print(nthPrime(100))

    # should return 7919.
    print(nthPrime(1000))

    # should return 104743.
    print(nthPrime(10001))
