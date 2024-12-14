from collections import defaultdict
import sys
import re
sys.setrecursionlimit(1073741824)

with open('day14_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    X = 101
    Y = 103

    robots = []
    for l in lines:
        matches = re.findall(r'p=(-*\d+),(-*\d+) v=(-*\d+),(-*\d+)', l)
        m = matches[0]
        px = int(m[0])
        py = int(m[1])
        vx = int(m[2])
        vy = int(m[3])
        robots.append([px, py, vx, vy])

    def p(rs):
        grid = []
        for _ in range(Y):
            grid.append(['.'] * X)
        for (px, py, _, _) in rs:
            grid[py][px] = 'X'
        for i in range(Y):
            print(''.join(grid[i]))

    def check(rs):
        seen = set()
        for (px, py, _ , _ ) in robots:
            seen.add((px, py))
        if len(seen) >= len(robots):
            return 1
        return 0

    for t in range(10000000):
        for i, (px, py, vx, vy) in enumerate(robots):
            px = (vx + px) % X
            py = (vy + py) % Y
            robots[i][0] = px
            robots[i][1] = py
        if check(robots):
            print(t + 1)
            p(robots)
            break

