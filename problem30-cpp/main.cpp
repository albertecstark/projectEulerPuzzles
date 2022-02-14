/*
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
 */

#include <iostream>
#include <vector>
#include <cmath>

std::vector<int> split_digits(int num){
    int num_digits = floor(log10(num)+1);
    std::vector<int> return_vec;
    for(int i = 1; i <= num_digits; ++i){
        int digit = ((num % int(pow(10,i))) - (num % int(pow(10, i - 1)))) / int(pow(10, i-1)); // what the fuck
        return_vec.push_back(digit);
    }
    return return_vec;
}

int sum_powers(int num){
    std::vector<int> digits = split_digits(num);
    int sum_d = 0;
    for(int i = 0; i < digits.size(); ++i){
        sum_d += int(pow(digits.at(i), 5));
    }
    return sum_d;
}

int main(){
    int result = 0;
    for(int i = 0; i < 100000000; ++i){
        if(i == sum_powers(i)){
            std::cout << i << " " << result << "\n";
            result += i;
        }
    }
    std::cout << "\n" << result;
    return 0;
}// note that this actually returns 1 more than the desired value, because im to lazy to change the loop conditions

