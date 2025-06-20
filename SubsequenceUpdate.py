t = int(input())
for _ in range(t):
    n,l,r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    k = r-l + 1
    ans = sum(a[:k])
    print(ans)