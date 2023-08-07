"""
p4_largest_palindrome_product.py:
    A palindrome number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""


def reverse(num):
    reversed_num = 0
    while num > 0:
        reversed_num = 10 * reversed_num + num % 10
        num //= 10

    return reversed_num


def is_palindrome(num):
    return num == reverse(num)


def calc_largest_palindrome():
    largest_palindrome = 0
    a = 999

    while a >= 100:

        if a % 11 == 0:
            b = 999
            db = 1
        else:
            b = 990  # The largest number less than or equal 999
            db = 11  # and divisible by 11

        while b >= a:

            if a * b <= largest_palindrome:
                break
            if is_palindrome(a * b):
                largest_palindrome = a * b
            b = b - db
        a -= 1

    return largest_palindrome


if __name__ == '__main__':
    print(calc_largest_palindrome())
