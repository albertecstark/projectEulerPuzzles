/*
Euler discovered the remarkable quadratic formula: n^2 + n + 41


It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=39. 
However, when n = 40, 40^40 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, 
which produces 80 primes for the consecutive values 0<=n<=79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n^2 + an + b
, where abs(a) < 1000 and abs(b) <= 1000

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes 
for consecutive values of n, starting with n = 0.
 */
using System;

namespace problem27
{
    class problem27
    {
        // loop through a, then loop through b inside a
        // if the first value is a prime then continue + check next, increment a counter + if it goes above the highest limit,
        // when it stops, check the last values, multiply them + make that the new highest
        bool is_prime(int x)
        {
            if (x==0 || x==1 || x==2)
            {
                return false;
            }
            for (int i = 1; i <= Math.Sqrt(x); i += 2)
            {
                if (x % i == 0)
                {
                    return false;
                }
            }
            return true;
        }

        public static int Main()
        {
            for (int a = 1; a < 1000; ++a)
            {
                for (int b = 1; b <= 1000; ++b)
                {
                    bool prime_return = true;
                    int test = 0;
                    while (prime_return == true)
                    {
                        // ¯\_(ツ)_/¯

                    }
                }
            }
            return 0;
        }
    }
}
