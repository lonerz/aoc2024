from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day23_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    adj = defaultdict(set)
    nodes = set()

    for l in lines:
        x,y = l.split('-')
        adj[x].add(y)
        adj[y].add(x)
        nodes.add(x)
        nodes.add(y)

    nodes = list(nodes)

    ans = 0
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            for k in range(j + 1, len(nodes)):
                x,y,z = nodes[i], nodes[j], nodes[k]
                if y in adj[x] and z in adj[x] and x in adj[y] and z in adj[y] and x in adj[z] and y in adj[z]:
                    if 't' in x[0] or 't' in y[0] or 't' in z[0]:
                        ans += 1
    print(ans)

