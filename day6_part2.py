from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day6_input.txt') as f:
    g = [l.strip() for l in f.readlines()]
    sx, sy = 0,0 
    R = len(g)
    C = len(g[0])
    for i in range(R):
        for j in range(C):
            if g[i][j] == '^':
                sx = i
                sy = j

    dirs = [[-1,0],[0,1],[1,0],[0,-1]]
    def dfs(sx, sy):
        di = 0
        visited = set()
        while 0 <= sx and sx < R and 0 <= sy and sy < C:
            if (sx, sy, di) in visited:
                return 0
            visited.add((sx, sy, di))
            nx = sx + dirs[di][0]
            ny = sy + dirs[di][1]
            while 0 <= nx < R and 0 <= ny < C and g[nx][ny] == '#':
                di = (di+1)%4
                nx = sx + dirs[di][0]
                ny = sy + dirs[di][1]
            sx, sy = nx, ny
        return 1

    ans = 0
    for i in range(R):
        for j in range(C):
            if g[i][j] == '#' or g[i][j] == '^':
                continue
            g[i][j] = '#'
            if not dfs(sx, sy):
                ans += 1
            g[i][j] = '.'
    print(ans)

