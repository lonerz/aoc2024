from collections import defaultdict
from itertools import permutations
import sys
sys.setrecursionlimit(1073741824)

def satisfy(o, ls):
    pos = {}
    for i,x in enumerate(o):
        pos[x] = i
    for l in ls:
        try:
            if pos[l[0]] >= pos[l[1]]:
                return 0
        except Exception:
            pass
    return 1

with open('day5_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    ans = 0
    check = 0
    limits = []
    orders = []
    for l in lines:
        if l == '':
            check = 1
            continue
        if check == 0:
            limits.append(list(map(int, l.split('|'))))
        else:
            orders.append(list(map(int, l.split(','))))
    for o in orders:
        if satisfy(o, limits):
            ans += o[len(o)//2]
    print(ans)

