import sys
sys.setrecursionlimit(1073741824)

with open('day25_input.txt') as f:
    line = f.read().strip()
    lines = line.split('\n\n')

    ls = []
    ks = []
    for l in lines:
        g = l.split('\n')

        s = []
        for j in range(len(g[0])):
            t = 0
            for i in range(len(g)):
                t += g[i][j] == '#'
            s.append(t - 1)

        if g[0][0] == '#': ls.append((s, len(g) - 2))
        else: ks.append((s, len(g) - 2))

    ans = 0
    for l in ls:
        for k in ks:
            f = 0
            for x,y in zip(k[0],l[0]):
                if x+y > k[1]: f = 1
            if not f:
                ans += 1
    print(ans)

