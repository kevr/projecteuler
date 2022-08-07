/*
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is

First ten:
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
*/
#include <iostream>
using namespace std;

const int N = 100;

int main()
{
    int square_sum = 0, total = 0;
    for(int i = 1; i <= N; ++i) {
        square_sum += i;
        total += i * i;
    }

    cout << (square_sum * square_sum) - total;

    return 0;
}