from collections import defaultdict, deque
import sys
sys.setrecursionlimit(1073741824)

DIR4 = [[0,1],[1,0],[0,-1],[-1,0]]

with open('day20_input.txt') as f:
    g = [list(l.strip()) for l in f.readlines()]
    R = len(g)
    C = len(g[0])

    sx,sy = -1,-1
    ex,ey = -1,-1
    for i in range(R):
        for j in range(C):
            if g[i][j] == 'S':
                sx,sy = i,j
                g[i][j] = '.'
            if g[i][j] == 'E':
                ex,ey = i,j
                g[i][j] = '.'

    front = {}
    q = deque([(sx,sy, 0)])
    while q:
        x,y,d = q.popleft()

        if (x,y) not in front:
            front[x,y] = d
        else:
            continue

        if x == ex and y == ey:
            break

        for i in range(4):
            dx,dy = DIR4[i]
            nx,ny = x+dx,y+dy
            if nx in range(R) and ny in range(C) and g[nx][ny] != '#':
                q.append((nx,ny,d+1))

    total = front[ex,ey]

    ans = 0
    for i in range(R):
        for j in range(C):
            if g[i][j] != '#':
                for dx, dy in DIR4:
                    nx1,ny1 = i+dx, j+dy
                    nx2,ny2 = i+2*dx, j+2*dy

                    if nx1 in range(R) and ny1 in range(C) and nx2 in range(R) and ny2 in range(C) and g[nx2][ny2] != '#':
                        temp = front[i,j] + 2 + total - front[nx2,ny2]
                        if total - temp >= 100:
                            ans += 1
    print(ans)

