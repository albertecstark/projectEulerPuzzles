# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# start by getting a number, parsing it into its digits as a list, exponentiating those, if the sum is equal to the original number, append these to a list of trues
import math

trues = []


def digits(x):
    dgt = list(str(x))
    return dgt


def main(limit):
    for i in range(limit):
        s = 0
        dgt = digits(i)
        for j in range(len(dgt)):
            s += math.pow(dgt[j], 5)
            if s == i:
                trues.append(s)
            #     print(f' appended {i}')
            # else:
            #     print(f'-- {i}')

    return trues


if '__name__' == '__main__':
    main(10000)
    print(sum(trues))
