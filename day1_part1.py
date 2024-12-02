import sys
sys.setrecursionlimit(1073741824)

with open('day1_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    a = []
    b = []
    for l in lines:
        x,y = map(int, l.split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    ans = 0
    for x,y in zip(a,b):
        ans += abs(x-y)
    print(ans)

