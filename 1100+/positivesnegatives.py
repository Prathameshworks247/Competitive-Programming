import sys
input = sys.stdin.readline

t = int(input())
out = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    neg = sum(1 for x in a if x < 0)
    total = sum(abs(x) for x in a)
    smallest = min(abs(x) for x in a)

    if neg % 2 == 0:
        out.append(total)
    else:
        out.append(total - 2 * smallest)

print('\n'.join(map(str, out)))