import sys
sys.setrecursionlimit(1073741824)

def okay(l):
    if l[0] == l[1]: return 0
    for i in range(len(l) - 1):
        if (l[0] - l[1]) * (l[i] - l[i+1]) <= 0: return 0
        if not (1 <= abs(l[i] - l[i+1]) <= 3): return 0
    return 1

with open('day2_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    ans = 0
    for l in lines:
        report = list(map(int, l.split()))
        if okay(report): ans += 1
    print(ans)

