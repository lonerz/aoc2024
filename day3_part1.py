from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day3_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    ans = 0
    for l in lines:
        xs = l.split('mul(')
        for x in xs:
            if ')' not in x: continue
            y = x.split(')')[0]
            if ',' not in y: continue
            try:
                a,b = map(int,y.split(','))
                ans += a*b
            except Exception:
                pass
    print(ans)

