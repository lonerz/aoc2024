import sys
sys.setrecursionlimit(1073741824)

def works(d, ts, seen):
    if len(d) == 0: return 1
    if d in seen:
        return seen[d]
    w = 0
    for t in ts:
        if len(d) >= len(t) and d.startswith(t):
            w = w or works(d[len(t):], ts, seen)
    seen[d] = w
    return w


with open('day19_input.txt') as f:
    line = f.read().strip()
    lines = line.split('\n\n')
    ts = lines[0].strip().split(', ')
    ds = [d.strip() for d in lines[1].split('\n')]

    seen = {}
    ans = 0
    for d in ds:
        if works(d, ts, seen): ans += 1
    print(ans)

