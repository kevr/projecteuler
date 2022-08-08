"""
Description: ProjectEuler Problem #14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Solution pseudocode:
    For each positive integer over 13 and under one million
        Find the number of memoized iterations in the Collatz sequence
    Return the length of the longest sequence found

Requirements:
    - We must test every single number in the iteration criteria
    - We can shortcut tests by relying on memoized lengths

Copyright (C) 2022 Kevin Morris <kevr@0cost.org>
All Rights Reserved.
"""
import sys
import traceback

# Global memo used for collatz sequence lengths
memo = dict()


def collatz_iteration(n: int) -> int:
    if n % 2 == 0:
        return n / 2
    return (3 * n) + 1


def collatz(c: int, n: int, i: int = 0) -> int:
    if c in memo:
        memo[n] = i + memo.get(c)
        return memo.get(n)
    elif c == 1:
        memo[n] = i
        return i

    c = collatz_iteration(c)
    return collatz(c, n, i + 1)


def main():
    longest: int = 0
    starting: int = 0

    for n in range(13, 1000000):
        length = collatz(n, n)
        if length > longest:
            longest = length
            starting = n

    print(f"{starting} = {longest}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(1)
