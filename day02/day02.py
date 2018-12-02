#!/usr/bin/env python3
from collections import Counter
from itertools import combinations

data = open('input.txt').readlines()
twos = sum(1 for x in [set(Counter(y).values()) for y in data] if 2 in x)
threes = sum(1 for x in [set(Counter(y).values()) for y in data] if 3 in x)
print(twos * threes)
for x, y in combinations(data, 2):
    diff = [i for i in range(len(x)) if x[i] != y[i]]
    if len(diff) == 1:
        print(x[:diff[0]] + x[diff[0]+1:])
        break
