from collections import defaultdict
import re
import sys
sys.setrecursionlimit(1073741824)

with open('day13_input.txt') as f:
    a = f.read()
    ts = a.split('\n\n')

    ans = 0
    for t in ts:
        ba, bb, p = t.strip().split('\n')

        m = re.findall(r'Button A: X\+(\d+), Y\+(\d+)', ba)
        bax, bay = int(m[0][0]), int(m[0][1])
        m = re.findall(r'Button B: X\+(\d+), Y\+(\d+)', bb)
        bbx, bby = int(m[0][0]), int(m[0][1])
        m = re.findall(r'Prize: X=(\d+), Y=(\d+)', p)
        px, py = int(m[0][0]), int(m[0][1])

        mn = 10000000
        for c1 in range(101):
            for c2 in range(101):
                if c1 * bax + c2 * bbx == px and c1 * bay + c2 * bby == py:
                    mn = min(3 * c1 + c2, mn)
        if mn != 10000000:
            ans += mn
    print(ans)

