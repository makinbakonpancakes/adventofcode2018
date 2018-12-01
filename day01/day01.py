#!/usr/bin/env python3
import itertools
data = [int(x) for x in open("input.txt").readlines()]
print(sum(data))

freq = 0
seen = set([0])
for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq); break
    seen.add(freq)
# print(next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f)))
