"""
p1_multiples_of_3_or_5.py:
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_divisible_by(divisor, target=999):
    p = target // divisor

    return divisor * (p * (p + 1)) / 2


if __name__ == '__main__':
    print(int(sum_divisible_by(3) +
              sum_divisible_by(5) -
              sum_divisible_by(3 * 5)))
