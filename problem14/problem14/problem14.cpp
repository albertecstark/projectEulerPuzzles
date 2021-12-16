/*
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
*/

#include <iostream>

int getCollatz(int sample) {
	int numIt = 0;
	while (sample != 1) {
		if (sample % 2 == 0) {
			sample = sample / 2;
		}
		else {
			sample = 3 * sample + 1;
		}
		++numIt;
	}
	return numIt;
}

int main() {
	int longestChain = 0;
	int longestStarter = 1;
	for (int i = 1; i < 100000; ++i) {
		getCollatz(i);
		if (getCollatz(i) > longestChain) {
			longestChain = getCollatz(i);
			longestStarter = i;
		}
	}
	std::cout << "\n" << longestStarter << "\n";
	return 0;
}