from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)

    x = max(freq, key=lambda v: (freq[v], v))
    cnt = freq[x]

    rest = n - cnt
    total = sum(a)

    if cnt <= rest + 2:
        print(total)
    else:
        print(total - (cnt - rest - 2) * x)