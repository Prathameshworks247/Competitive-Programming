T= int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split())) 
    pref = [0]*n
    summ = 0
    ans= 0
    for i in range(n):
        summ += a[i]
        pref[i] += summ
    for k in range(1,n+1):
        if n % k != 0:
            continue
        start = k - 1
        mini =  pref[start]
        maxi = pref[start]
        for i in range(start + k, n, k):
            curr = pref[i] - pref[i - k]
            mini = min(mini, curr)
            maxi = max(maxi, curr)
        ans = max(ans, maxi - mini)
        
    print(ans)
        
        
        
        
