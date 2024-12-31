import sys
sys.setrecursionlimit(1073741824)

with open('day24_input.txt') as f:
    line = f.read().strip()
    lines = line.split('\n\n')

    vs = {}
    for v in lines[0].split('\n'):
        k,val = v.split(': ')
        val = int(val)
        vs[k] = val

    es = []
    for eq in lines[1].split('\n'):
        a, out = eq.split(' -> ')
        c1, op, c2 = a.split(' ')
        es.append((out, c1, op, c2))

    def comp(c1, op, c2):
        if op == 'AND': return c1 & c2
        if op == 'OR': return c1 | c2
        if op == 'XOR': return c1 ^ c2

    while es:
        nw = []
        for e in es:
            out, c1, op, c2 = e
            if c1 in vs and c2 in vs:
                vs[out] = comp(vs[c1], op, vs[c2])
            else:
                nw.append(e)
        es = nw

    outputs = []
    for v in vs:
        if v[0] == 'z':
            outputs.append((v, vs[v]))
    outputs.sort(reverse=True)

    b = ''
    for _, o in outputs:
        b += str(o)
    print(int(b, 2))

