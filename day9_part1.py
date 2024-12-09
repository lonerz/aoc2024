from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day9_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    s = lines[0]

    r = []
    j = 0
    for i,x in enumerate(s):
        if i % 2 == 0:
            r.extend([j] * int(x))
            j += 1
        else:
            r.extend(['.'] * int(x))

    j = len(r) - 1
    while j > 0:
        i = 0
        while i < j:
            if r[i] == '.':
                r[i] = r[j]
                r[j] = '.'
                break
            i += 1
        # couldn't move
        if i == j:
            break
        while r[j] == '.':
            j -= 1

    ans = 0
    i = 0
    for x in r:
        if x == '.':
            continue
        ans += i * x
        i += 1
    print(ans)

