
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
"""

def multiplesOf3and5(number):
    soma = 0
    for x in range(1, number):
        if x % 3 == 0 or x % 5 == 0:
            soma += x
    return soma


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

