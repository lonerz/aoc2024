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

        # left and right is easy
        if dx == 0:
            ty = ny
            while g[nx][ty] in {'[', ']'}:
                ty += dy
            if g[nx][ty] == '.':
                while ty - dy != y:
                    g[nx][ty] = '[' if dy < 0 else ']'
                    g[nx][ty - dy] = ']' if dy < 0 else '['
                    ty -= 2 * dy
                g[nx][ny] = '@'
                g[x][y] = '.'
                return nx, ny
            return x, y

        # up/down, not so much...
        def find_box(bx, by, dx):  # bx, by is [
            if g[bx + dx][by] == '#' or g[bx + dx][by + 1] == '#':
                return 0, []

            next_two = [g[bx + dx][by], g[bx + dx][by + 1]]
            if next_two == ['.', '.']:
                return 1, [(bx, by)]

            # one box
            if next_two == ['[', ']']:
                w, boxes = find_box(bx + dx, by, dx)
                return w, boxes + [(bx, by)]
            if next_two == ['.', '[']:
                w, boxes = find_box(bx + dx, by + 1, dx)
                return w, boxes + [(bx, by)]
            if next_two == [']', '.']:
                w, boxes = find_box(bx + dx, by - 1, dx)
                return w, boxes + [(bx, by)]

            # two boxes
            if next_two == [']', '[']:
                w1, b1 = find_box(bx + dx, by - 1, dx)
                w2, b2 = find_box(bx + dx, by + 1, dx)
                return w1 and w2, b1 + b2 + [(bx, by)]

            return 0, [(bx, by)]

        if g[nx][ny] == ']':
            works, boxes = find_box(nx, ny - 1, dx)
        else:
            works, boxes = find_box(nx, ny, dx)

        # aghhhh
        if works:
            boxes.sort()
            if dx > 0: boxes = boxes[::-1]
            # move each box
            for cx, cy in boxes:
                g[cx + dx][cy] = '['
                g[cx + dx][cy + 1] = ']'
                g[cx][cy] = g[cx][cy + 1] = '.'
            g[nx][ny] = '@'
            g[x][y] = '.'
            return nx, ny

        return x, y

    new_g = []
    for i in range(R):
        new_g.append([])
        for j in range(C):
            if g[i][j] == '#':
                new_g[-1] += ['#', '#']
            if g[i][j] == 'O':
                new_g[-1] += ['[', ']']
            if g[i][j] == '.':
                new_g[-1] += ['.', '.']
            if g[i][j] == '@':
                new_g[-1] += ['@', '.']
    g = new_g

    sx, sy = -1, -1
    for i in range(R):
        for j in range(2 * C):
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
        for j in range(2 * C):
            if g[i][j] == '[':
                ans += i * 100 + j
    print(ans)

