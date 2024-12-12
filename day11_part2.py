from collections import defaultdict
import sys
sys.setrecursionlimit(1073741824)

with open('day11_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    s = list(map(int,lines[0].split()))

    memo = {}  # (start, length) -> # of stones
    def dfs(start, l):
        if (start, l) in memo:
            return memo[(start, l)]
        if l == 75:
            memo[(start, l)] = 1
            return 1
        if start == 0:
            memo[(start, l)] = t = dfs(1, l + 1)
            return t
        m = str(start)
        if len(m) % 2 == 0:
            memo[(start, l)] = t = dfs(int(m[:len(m)//2]), l + 1) + dfs(int(m[len(m)//2:]), l + 1)
            return t
        memo[(start, l)] = t = dfs(2024 * start, l + 1)
        return t

    ans = 0
    for x in s:
        ans += dfs(x, 0)
    print(ans)

