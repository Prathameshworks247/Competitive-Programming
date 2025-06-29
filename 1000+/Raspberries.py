T= int(input())

for _ in range(T):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    diff = 0
    ans = float("inf")
    for i in a:
        if i%k == 0:
            ans = 0
            break
        ans = min(ans, k-(i%k))
    if k == 4:
        even = 0
        odd = 0
        for i in a:
            if i%2 == 0:
                even += 1
            else:
                odd += 1
        if even > 1:
            ans = min(ans, 0)
        elif even == 1:
            ans = min(ans, 1)
        elif even ==0:
            ans = min(ans, 2)
    print(ans)