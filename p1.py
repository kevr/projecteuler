#!/usr/bin/env python3
""" https://projecteuler.net/problem=1 """
n = 1000

items = set()
for i in range(2, n):
    if i % 3 == 0 or i % 5 == 0:
        items.update({i})

print(sum(items))
