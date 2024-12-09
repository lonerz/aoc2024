from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day7_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    ans = 0
    for l in lines:
        l = l.split(': ')
        result = int(l[0])
        ops = list(map(int, l[1].split(' ')))
        x = len(ops) - 1
        for t in range(int(2 ** x)):
            temp = t
            r = ops[0]
            i = 1
            while temp or i <= x:
                if temp % 2: r *= ops[i]
                else: r += ops[i]
                temp //= 2
                i += 1
            if r == result:
                ans += result
                break
    print(ans)

