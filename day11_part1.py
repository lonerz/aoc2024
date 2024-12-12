from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day11_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    s = list(map(int,lines[0].split()))
    for _ in range(25):
        new = []
        for i,x in enumerate(s):
            m = str(x)
            if x == 0: new.append(1)
            elif len(m) % 2 == 0:
                new.append(int(m[:len(m)//2]))
                new.append(int(m[len(m)//2:]))
            else: new.append(2024 * x)
        s = new
    print(len(s))

