"""
p3_largest_prime_factor.py:
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143?
"""

import math


def largest_prime_factor(number):
    if number % 2 == 0:
        last_factor = 2
        number /= 2

        while number % 2 == 0:
            number /= 2
    else:
        last_factor = 1

    factor = 3
    max_factor = math.sqrt(number)

    while number > 1 and factor <= max_factor:
        if number % factor == 0:
            number = number / factor
            last_factor = factor
            while number % factor == 0:
                number /= factor
            max_factor = math.sqrt(number)
        factor += 2

    if number == 1:
        return int(last_factor)
    else:
        return int(number)


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
