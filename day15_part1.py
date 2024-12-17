import sys
sys.setrecursionlimit(1073741824)

DIR4 = [[0,1],[1,0],[0,-1],[-1,0]]

with open('day15_input.txt') as f:
    line = f.read().strip()
    lines = line.split('\n\n')

    g = [list(l.strip()) for l in lines[0].split()]
    moves = lines[1]

    chars = ['>', 'v', '<', '^']
    R = len(g)
    C = len(g[0])

    def move(x, y, dx, dy):
        nx, ny = x+dx, y+dy
        if g[nx][ny] == '#':
            return x, y
        if g[nx][ny] == '.':
            g[nx][ny] = '@'
            g[x][y] = '.'
            return nx, ny
        tx,ty = nx,ny
        while g[tx][ty] == 'O':
            tx += dx
            ty += dy
        if g[tx][ty] != '#':
            g[tx][ty] = 'O'
            g[nx][ny] = '@'
            g[x][y] = '.'
            return nx, ny
        return x, y

    sx, sy = -1, -1
    for i in range(R):
        for j in range(C):
            if g[i][j] == '@':
                sx,sy = i,j

    for m in moves:
        if m not in chars:
            continue
        i = chars.index(m)
        dx, dy = DIR4[i]
        sx, sy = move(sx, sy, dx, dy)

    ans = 0
    for i in range(R):
        for j in range(C):
            if g[i][j] == 'O':
                ans += i * 100 + j
    print(ans)

