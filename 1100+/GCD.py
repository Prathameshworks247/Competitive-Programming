import sys
from math import gcd

input = sys.stdin.readline

t = int(input())
out = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)
    prefix = 0
    best = 0

    for i in range(n - 1):        # cut after index i, both parts non-empty
        prefix += a[i]
        best = max(best, gcd(prefix, total - prefix))

    out.append(best)

print('\n'.join(map(str, out)))