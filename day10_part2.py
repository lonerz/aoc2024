from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day10_input.txt') as f:
    g = [list(map(int,l.strip())) for l in f.readlines()]
    R = len(g)
    C = len(g[0])
    def dfs(x,y, n):
        if x not in range(R) or y not in range(C) or g[x][y] != n:
            return 0
        if n == 9:
            return 1
        ans = 0
        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            ans += dfs(x+dx, y+dy, n + 1)
        return ans
    ans = 0
    for i in range(R):
        for j in range(C):
            if g[i][j] == 0:
                ans += dfs(i, j, 0)
    print(ans)

