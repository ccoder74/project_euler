"""
p5_smallest_multiple.py:
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all
    of the numbers from 1 to 20?
"""

from functools import reduce


def evenly_divisible(n):
    multipliers = []

    for i in range(1, n + 1):
        current_number = i

        for element in multipliers:
            if current_number % element == 0:
                current_number = int(current_number / element)

        multipliers.append(current_number)

    return multipliers


def smallest_multiple(n):
    list_nums = evenly_divisible(n)

    return reduce(lambda a, b: a * b, list_nums)


if __name__ == '__main__':
    pos_int = input('Enter a positive integer: ')
    print('The smallest positive number that is evenly divisible by', end=" ")
    print(f'all of the numbers from 1 to {pos_int} is:', end=" ")
    print(smallest_multiple(20))
