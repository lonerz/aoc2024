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

def order(o, ls):
    q = [[o[0]]]
    for j in range(1, len(o)):
        x = o[j]
        temp = []
        for a in q:
            for i in range(len(a) + 1):
                if satisfy(a[:i] + [x] + a[i:], ls):
                    temp.append(a[:i] + [x] + a[i:])
        q = temp
    return q[0][len(q[0])//2]

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
        if not satisfy(o, limits):
            ans += order(o, limits)
    print(ans)

