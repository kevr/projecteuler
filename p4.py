#!/usr/bin/env python3
""" https://projecteuler.net/problem=4 """


def max_palindrome(lower_bound: int, upper_bound: int) -> int:
    """ Return largest palindrome product from lower_bound to upper_bound. """
    largest = 0  # Largest value matched
    for x in range(lower_bound, upper_bound):
        for y in range(lower_bound, upper_bound):
            value = x * y
            string = str(value)
            # If the resulting string is a palindrome.
            if string == string[::-1]:
                # If the current value is larger than our largest.
                if value > largest:
                    # Update our locals.
                    largest = value
    return largest


print(max_palindrome(100, 1000))
