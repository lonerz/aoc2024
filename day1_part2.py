from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day1_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    a = []
    b = defaultdict(int)
    for l in lines:
        x,y = map(int, l.split())
        a.append(x)
        b[y] += 1
    ans = 0
    for x in a:
        ans += b[x] * x
    print(ans)

