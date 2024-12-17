import sys
import re
sys.setrecursionlimit(1073741824)

with open('day17_input.txt') as f:
    line = f.read().strip()
    lines = line.split('\n\n')

    rs = lines[0].split('\n')
    ra = rs[0].strip()
    a = int(re.findall('Register A: (\d+)', ra)[0])
    rb = rs[1].strip()
    b = int(re.findall('Register B: (\d+)', rb)[0])
    rc = rs[2].strip()
    c = int(re.findall('Register C: (\d+)', rc)[0])

    p = lines[1].strip()
    pm = re.findall('Program: (.*)', p)
    ops = list(map(int,pm[0].split(',')))

    def dfs(last_a, sol, i):
        if len(sol) == len(ops):
            return last_a
        mn = -1
        for A in range(8 * last_a, 8 * last_a + 8):
            # hand derived the formula from my program
            B = (A % 8) ^ 1
            if ((B^5)^(A//int(2**B))) % 8 == ops[i]:
                t = dfs(A, [last_a] + sol, i - 1)
                if t != -1:
                    mn = t if mn == -1 else min(mn, t)
        return mn

    print(dfs(0, [], len(ops) - 1))

