'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

x = 600851475143

def largestPrimeFactors(x):
    primeFactors = []
    for i in range(3, int(math.sqrt(x)), 2):
        while(x % i == 0):
            primeFactors.append(i)
            x = x / i
    print(primeFactors)

largestPrimeFactors(x)
