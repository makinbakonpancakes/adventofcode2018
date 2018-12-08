from datetime import datetime
import re
from collections import defaultdict

data = [(datetime.strptime(x[1:17], "%Y-%m-%d %H:%M"), x[19:-1])
         for x in open('input.txt').readlines()]
data = sorted(data, key=lambda x: x[0])
guards = defaultdict(lambda: [0 for x in range(60)])
for d in data:
    if "#" in d[1]:
        guard = int(re.search(r'#(\d+)', d[1]).group(1))
    elif "asleep" in d[1]:
        sleep = d[0].minute
    else:
        awake = d[0].minute
        for x in range(sleep, awake):
            guards[guard][x] += 1
sleepy = sorted(guards.keys(), key=lambda g: -sum(guards[g]))[0]
print(sleepy * guards[sleepy].index(max(guards[sleepy])))
sleepy2 = sorted(guards.keys(), key=lambda g: -max(guards[g]))[0]
print(sleepy2 * guards[sleepy2].index(max(guards[sleepy2])))
