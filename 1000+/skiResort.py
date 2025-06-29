T = int(input())
for _ in range(T):
    n,k,q = map(int, input().split())
    a = list(map(int, input().split()))
    temp = []
    count = 0
    ans = 0
    for i in range(n):
        if a[i] <= q:
            count += 1
        else:
            temp.append(count)
            count = 0
    temp.append(count)

    for i in temp:
        if i >= k:
            for j in range(k, i + 1):
                ans += (i - j + 1)
    print(ans)