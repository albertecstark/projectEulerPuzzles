/*
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
*/
#include <iostream>
using namespace std;

int main() {
    int n, t1 = 0, t2 = 1, nextTerm = 0;
    n = 35;
    int evenSum = 0;
    for (int i = 1; i <= n; ++i) {
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
        if (nextTerm % 2 == 0) {
            evenSum += nextTerm;
        }
        if(nextTerm > 4000000){
            break;
        }
    }
    cout << "\nthe sum of even fibonnaci numbers bellow 4,000,000 is:" << evenSum;
    return 0;
}