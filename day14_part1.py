from collections import defaultdict
import sys
import re
import time
sys.setrecursionlimit(1073741824)

with open('day14_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    X = 101
    Y = 103

    ans = 0
    robots = []
    for l in lines:
        matches = re.findall(r'p=(-*\d+),(-*\d+) v=(-*\d+),(-*\d+)', l)
        m = matches[0]
        px = int(m[0])
        py = int(m[1])
        vx = int(m[2])
        vy = int(m[3])
        robots.append([px, py, vx, vy])

    for t in range(100):
        for i, (px, py, vx, vy) in enumerate(robots):
            px = (vx + px) % X
            py = (vy + py) % Y
            robots[i][0] = px
            robots[i][1] = py

    q = [0, 0, 0, 0]
    for (px, py, _ , _) in robots:
        if px < X // 2 and py < Y // 2: q[0] += 1
        if px < X // 2 and py > Y // 2: q[1] += 1
        if px > X // 2 and py > Y // 2: q[2] += 1
        if px > X // 2 and py < Y // 2: q[3] += 1
    print(q[0] * q[1] * q[2] * q[3])

