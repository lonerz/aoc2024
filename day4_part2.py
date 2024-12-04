from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

def okay(d, h, w):
    return 0 <= d[0] < h and 0 <= d[1] < w

with open('day4_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    ans = 0
    H = len(lines)
    W = len(lines[0])
    for i in range(H):
        for j in range(W):
            if lines[i][j] == 'A':
                d11 = i-1,j-1
                d12 = i+1,j+1
                d21 = i+1,j-1
                d22 = i-1,j+1
                if okay(d11, H, W) and okay(d12, H, W) and okay(d22, H, W) and okay(d21, H, W):
                    if (
                        {lines[d11[0]][d11[1]], lines[d12[0]][d12[1]]} == {'M', 'S'}
                        and {lines[d21[0]][d21[1]], lines[d22[0]][d22[1]]} == {'M', 'S'}
                    ):
                        ans += 1
    print(ans)


