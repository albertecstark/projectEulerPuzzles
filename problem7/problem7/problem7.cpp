/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
 */
#include <iostream>

bool isPrime(int p)
{
	if(p==0||p==1) return false;

	for(int i = 2; i < static_cast<int>(sqrt(p)) + 1; ++i)
	{
		if(p % i == 0) return false;
	}

	return true;
}

int main()
{
	int k = 0;
	while(k<105000)
	{
		if(isPrime(k) == true)
		{
			std::cout << k << "\n";
		}
		++k;
	}
}