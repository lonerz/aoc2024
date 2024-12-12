from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day12_input.txt') as f:
    g = [list(l.strip()) for l in f.readlines()]

    R = len(g)
    C = len(g[0])

    visited = set()
    def dfs(x,y,t):
        if x not in range(R) or y not in range(C) or g[x][y] != t:
            return 0, 0
        if (x,y) in visited:
            return 0, 0
        visited.add((x,y))

        e = g[x][y]
        assert e != '.'

        corners = 0
        area = 1
        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            a, c = dfs(x+dx,y+dy,t)
            area += a
            corners += c

        is_corner = 0
        for check in [[[0,1],[1,1],[1,0]], [[0,1],[-1,1],[-1,0]], [[0,-1],[-1,-1],[-1,0]], [[0,-1],[1,-1],[1,0]]]:
            corner = ''
            for dx,dy in check:
                nx,ny = x+dx, y+dy
                if nx not in range(R) or ny not in range(C):
                    corner += '.'
                else:
                    corner += g[nx][ny]

            if corner[0] != e and corner[2] != e:
                is_corner += 1
            elif corner[0] == e and corner[2] == e and corner[1] != e:
                is_corner += 1

        return area, corners + is_corner

    ans = 0
    for i in range(R):
        for j in range(C):
            if (i,j) not in visited:
                a, c = dfs(i,j,g[i][j])
                ans += a*c
    print(ans)

