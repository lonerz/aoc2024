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
            return 0, 1
        if (x,y) in visited:
            return 0, 0
        visited.add((x,y))

        area = 1
        perimeter = 0
        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            a, p = dfs(x+dx,y+dy,t)
            area += a
            perimeter += p

        return area, perimeter

    ans = 0
    for i in range(R):
        for j in range(C):
            if (i,j) not in visited:
                a, p = dfs(i,j,g[i][j])
                ans += a*p
    print(ans)

