/**
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10001st prime number?
**/
#include <iostream>
#include <cstdlib>
#include <unordered_map>
#include <cmath>
#include <list>
using namespace std;

using std::size_t;

const size_t PRIMES = 10001;

uint64_t prime(uint64_t n)
{
    const uint64_t N = (uint64_t)sqrt(n) + 1;
    for(uint64_t i = 2; i <= N; ++i)
        if(n % i == 0)
            return false;
    return true;
}

int main()
{
    uint64_t last = 2;
    std::list<uint64_t> primes;
    for(uint64_t i = 0; primes.size() <= PRIMES; ++i) {
        if(prime(i)) {
            primes.push_back(i);
        }
    }
    std::cout << primes.back() << std::endl;

    return 0;
}