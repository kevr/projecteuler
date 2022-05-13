#!/usr/bin/env python3
""" https://projecteuler.net/problem=2 """
N: int = 4000000  # Term upper-bound.

x: int = 1  # Left hand side term
y: int = 2  # Right hand side term
total: int = 0  # Total accumulation of even terms

# While our RHS is within range
while y <= N:
    # If our RHS is even
    if y % 2 == 0:
        # Add it to the total
        total += y
    # Increment terms based on Fibonacci
    x, y = y, x + y

# Print out the total
print(total)
