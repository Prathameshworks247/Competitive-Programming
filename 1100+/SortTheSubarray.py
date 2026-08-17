t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a2 = list(map(int,input().split()))
    
    l = 0
    while l < n and a[l] == a2[l]:
        l += 1

    if l == n:
        print(1, 1)
        continue

    r = l
    for i in range(l, n):
        if a[i] != a2[i]:
            r = i

    while l > 0 and a2[l] >= a2[l-1]:
        l -= 1

    while r < n-1 and a2[r] <= a2[r+1]:
        r += 1

    print(l+1, r+1)