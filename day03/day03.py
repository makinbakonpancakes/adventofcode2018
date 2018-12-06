#!/usr/bin/env python3
import re
from collections import defaultdict
from itertools import product

data = [[int(y.strip('# ')) for y in re.split("[@,:x]", x)]
        for x in open('input.txt').readlines()]
grid = defaultdict(lambda: defaultdict(lambda: [0,0]))
overlap = 0
dirty = set()
for claim in data:
    for x, y in product(range(claim[3]), range(claim[4])):
        grid_value = grid[claim[1] + x][claim[2] + y]
        if  grid_value[1] == 1:
            overlap += 1
        if grid_value[1] >= 1:
            dirty.add(grid_value[0])
            dirty.add(claim[0])
        grid_value[0] = claim[0]
        grid_value[1] += 1
print(overlap)
print([x[0] for x in data if x[0] not in dirty][0])
