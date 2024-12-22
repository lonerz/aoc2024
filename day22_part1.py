import sys
sys.setrecursionlimit(1073741824)

with open('day22_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    def s(x):
        MOD = 16777216
        x ^= x * 64
        x %= MOD
        x ^= x // 32
        x %= MOD
        x ^= x * 2048
        x %= MOD
        return x

    ans = 0
    for l in lines:
        x = int(l)
        for _ in range(2000):
            x = s(x)
        ans += x
    print(ans)

