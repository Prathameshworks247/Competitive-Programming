T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))

    curr = a[0]
    ans = a[0]

    for i in range(1, n):
        if a[i] % 2 != a[i-1] % 2:   # alternating parity
            curr = max(a[i], curr + a[i])  # extend or restart
        else:
            curr= a[i]
        ans = max(ans, curr)           # update best answer


    print(ans)
    
    
