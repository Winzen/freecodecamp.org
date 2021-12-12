#LINK PROBLEM: https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-3-largest-prime-factor
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the given number?
"""

def largestPrimeFactor(number):

    i = max = 2
    while number >= i:
        if number % i == 0:
            max = i
            number = number / i
        else:
            i += 1
    return max


if __name__ == '__main__':
    #should return 2.
    print(largestPrimeFactor(2))

    # should return 3.
    print(largestPrimeFactor(3))

    # should return 5.
    print(largestPrimeFactor(5))

    # should return 7.
    print(largestPrimeFactor(7))

    # should return 2.
    print(largestPrimeFactor(8))

    # should return 29.
    print(largestPrimeFactor(13195))

    # should return 6857.
    print(largestPrimeFactor(600851475143))