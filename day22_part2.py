from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day22_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    def s(x):
        MOD = 16777216
        x ^= x * 64
        x %= MOD
        x ^= x // 32
        x %= MOD
        x ^= x * 2048
        x %= MOD
        return x

    ans = 0
    argh = defaultdict(lambda: {})
    for t,l in enumerate(lines):
        x = int(l)
        ps = []
        for _ in range(2001):
            ps.append(x%10)
            x = s(x)

        diffs = []
        for i in range(2000):
            diffs.append((ps[i + 1] - ps[i], ps[i + 1]))

        for i in range(len(diffs)):
            lst = diffs[i:i+4]
            if len(lst) == 4:
                ind = ''.join(map(str, [x[0] for x in lst]))
                if t not in argh[ind]:
                    argh[ind][t] = lst[-1][1]

    mx = 0
    for ind in argh:
        bs = 0
        for j in argh[ind]:
            bs += argh[ind][j]
        mx = max(mx, bs)
    print(mx)

