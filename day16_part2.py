from collections import defaultdict
import heapq
import sys
sys.setrecursionlimit(1073741824)

DIR4 = [[0,1],[1,0],[0,-1],[-1,0]]

with open('day16_input.txt') as f:
    g = [list(l.strip()) for l in f.readlines()]
    R = len(g)
    C = len(g[0])

    sx, sy = -1, -1
    ex, ey = -1, -1
    for i in range(R):
        for j in range(C):
            if g[i][j] == 'S':
                sx, sy = i, j
            if g[i][j] == 'E':
                ex, ey = i, j

    def pad(x):
        return '0' * (3 - len(str(x))) + str(x)

    new_g = defaultdict(lambda: defaultdict(int))
    for i in range(R):
        for j in range(C):
            for curd in range(4):
                node = pad(i) + pad(j) + str(curd)

                for otherd in [curd, (curd + 1) % 4, (curd + 3) % 4]:
                    dx, dy = DIR4[otherd]
                    ni, nj = i + dx, j + dy
                    if ni in range(R) and nj in range(C) and g[ni][nj] != '#':
                        nxt = pad(ni) + pad(nj) + str(otherd)
                        new_g[node][nxt] = 1 if curd == otherd else 1001

    MX = 10000000000000
    dist = defaultdict(lambda: MX)
    pq = []
    prev = defaultdict(list)
    for d in range(4):
        start = pad(sx) + pad(sy) + str(d)
        if d == 0: w = 0
        if d == 1 or d == 3: w = 1000
        if d == 2: w = 2000
        heapq.heappush(pq, (w, start))
        dist[start] = w

    while pq:
        _, v = heapq.heappop(pq)
        for nxt, d in new_g[v].items():
            if dist[nxt] > dist[v] + d:
                dist[nxt] = dist[v] + d
                heapq.heappush(pq, (dist[nxt], nxt))
                prev[nxt] = [v]
            elif dist[nxt] == dist[v] + d:
                prev[nxt].append(v)

    mn, md = MX, ''
    for d in range(4):
        end = pad(ex) + pad(ey) + str(d)
        if dist[end] < mn:
            mn = dist[end]
            md = end

    tiles = set()
    def dfs(node):
        x,y = int(node[0:3]), int(node[3:6])
        tiles.add((x,y))
        for p in prev[node]:
            dfs(p)
    dfs(md)
    print(len(tiles))

