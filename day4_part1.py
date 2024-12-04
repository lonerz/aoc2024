from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day4_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    ans = 0
    H = len(lines)
    W = len(lines[0])
    for i in range(H):
        for j in range(W):
            if lines[i][j] == 'X':
                for dx, dy in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
                    i1,j1 = i+dx,j+dy
                    i2,j2 = i+dx*2,j+dy*2
                    i3,j3 = i+dx*3,j+dy*3
                    if 0<=i1<H and 0<=j1<W and 0<=i2<H and 0<=j2<W and 0<=i3<H and 0<=j3<W:
                        if lines[i1][j1] == 'M' and lines[i2][j2] == 'A' and lines[i3][j3] == 'S':
                            ans += 1
    print(ans)


