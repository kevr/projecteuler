#!/usr/bin/env python3
""" https://projecteuler.net/problem=3 """
from math import sqrt
from typing import Dict

# The target of the task.
TARGET: int = 600851475143

# Take the square root of TARGET, which gives us the prime
# upper bound for TARGET. We can then use this upper bound
# to iterate through a subset of TARGET while factoring.
N: int = int(sqrt(TARGET) + 1)

# Build a Sieve of Eratosthenes up to N:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
sieve: Dict[int, bool] = dict()

# First, set 2..N + 1 to True in our sieve.
for i in range(2, N + 1):
    sieve[i] = True

# Then, iterate through and set all of our non-primes to False.
for i in range(2, N + 1):
    if sieve.get(i):
        j: int = i ** 2
        m: int = 0
        while j <= N:
            sieve[j] = False
            j, m = (i * i) + (i * m), m + 1

# Now that we've decided who our primes are, create a sorted
# and reversed set of primes. We will iterate from 0..n, where
# 0 is the highest prime found and n is the lowest (2).
sieve = list(sorted([k for k, v in sieve.items() if v], reverse=True))

# Now, get our target factor by testing TARGET against each
# sieve element. Quit out when we find it.
fact: int = 0
for factor in sieve:
    if TARGET % factor == 0:
        fact = factor
        break

# Print the factor out.
print(fact)
