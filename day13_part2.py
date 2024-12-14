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

        px += 10000000000000
        py += 10000000000000

        if (px * bay - py * bax) % (bbx * bay - bby * bax): continue
        y = (px * bay - py * bax) // (bbx * bay - bby * bax)

        if (py - y * bby) % bay: continue
        x = (py - y * bby) // bay
        ans += 3 * x + y

    print(ans)

