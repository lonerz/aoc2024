import networkx as nx
import sys
sys.setrecursionlimit(1073741824)

with open('day23_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    G = nx.Graph()

    for l in lines:
        x,y = l.split('-')
        G.add_edge(x, y)

    mx = []
    for x in nx.find_cliques(G):
        if len(x) > len(mx):
            mx = x
    mx.sort()
    print(','.join(mx))

