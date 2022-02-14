# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
import math


def split_digits(num):
    split_digits_list = []
    num_digits = math.floor(math.log(num, 10) + 1)
    for i in range(0, num_digits):
        digit = num % 10 ** i - num % 10 ** (i - 1)
        digit / 10 ** (i - 1)
        split_digits_list.append(digit)
    return split_digits_list


def sum_powers(num):
    digits = split_digits(num)
    sum_d = 0
    for i in range(0, len(digits)):
        sum_d += digits[i] ** 5
    return sum_d


def main():
    result = 0
    for i in range(1, 100000000):
        if i == sum_powers(i):
            print(str(i) + " " + str(result) + "\n")
            result += i
    return 0


if __name__ == "__main__":
    main()
