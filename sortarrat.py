n = int(input())

a = list(map(int, input().split()))

s = sorted(a)

diff  = [(a[i] - s[i]) for i in range(n)]


