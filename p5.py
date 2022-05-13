#!/usr/bin/env python3
""" https://projecteuler.net/problem=5 """


def min_divisor(a: int, b: int) -> int:
    i: int = b
    done: bool = False
    while not done:
        # Step up +b.
        i += b

        # For a..b
        for j in range(a, b):
            # If j does not divide into i, we are not done.
            done = (i % j == 0)
            if not done:
                # Since we're not done on this i, break out.
                break

    # Return the i we ended up at.
    return i


print(min_divisor(1, 20))
