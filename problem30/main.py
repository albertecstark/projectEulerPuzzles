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
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# start by getting a number, parsing it into its digits as a list, exponentiating those,
#       if the sum is equal to the original number,
#               append these to a list of trues
#
# This method isn't at all rigorous, but if I test to a high enough value, and new values stop appearing,
#   then I can assume that this is correct
# I have tested up to 10,000,000 which returned the same as 1,000,000 , which was the same as 200,000
#   hopefully it's not the case that there is in fact a next term, and I need to go further
# TODO: attach images of the proof that I think of that this is in fact correct
import math

trues = []


def digits(x):
    dgt = list(str(x))
    return dgt


def main(limit):
    for i in range(2, limit):
        # remember, 1 doesn't count as a valid solution
        s = 0
        dgt = digits(i)
        for j in range(len(dgt)):
            val = math.pow(int(dgt[j]), 4)
            s += val
            if s == i:
                trues.append(s)
                print(f' appended {i}')
            else:
                print(f'-- {i}')

    print(trues)
    print(sum(trues))
    sum_dgt = sum(trues)
    return sum_dgt


user_in = input('please type the number that you want to test up to (integer)')

main(int(user_in))
