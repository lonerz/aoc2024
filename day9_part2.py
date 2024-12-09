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
            r.append([j, int(x)])
            j += 1
        else:
            r.append(['.', int(x)])

    j = len(r) - 1
    while j > 0:
        i = 0
        while i < j:
            if r[i][0] == '.' and r[i][1] >= r[j][1]:
                r[i][0] = r[j][0]
                r[j][0] = '.'

                diff = r[i][1] - r[j][1]
                if diff:
                    r[i][1] = r[j][1]
                    r.insert(i + 1, ['.', diff])
                    j += 1
                break
            i += 1
        # couldn't move
        if i == j:
            j -= 1
        while r[j][0] == '.':
            j -= 1

    ans = 0
    i = 0
    for x in r:
        if x[0] == '.':
            i += x[1]
            continue
        for t in range(x[1]):
            ans += i * x[0]
            i += 1
    print(ans)

