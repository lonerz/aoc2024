from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day8_input.txt') as f:
    g = [list(l.strip()) for l in f.readlines()]

    ats = defaultdict(list)
    R = len(g)
    C = len(g[0])
    for i in range(R):
        for j in range(C):
            if g[i][j] == '.':
                continue
            ats[g[i][j]].append((i,j))

    antinodes = set()
    for at in ats:
        freqs = ats[at]
        for i in range(len(freqs)):
            for j in range(i + 1, len(freqs)):
                dx = freqs[i][0] - freqs[j][0]
                dy = freqs[i][1] - freqs[j][1]
                nx, ny = freqs[i]
                while 0 <= nx < R and 0 <= ny < C:
                    antinodes.add((nx, ny))
                    nx += dx
                    ny += dy

                dx = -dx
                dy = -dy
                mx, my = freqs[j]
                while 0 <= mx < R and 0 <= my < C:
                    antinodes.add((mx, my))
                    mx += dx
                    my += dy

    print(len(antinodes))

