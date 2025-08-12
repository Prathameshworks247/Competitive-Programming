t = int(input())

for _ in range(t):
    n,x  = map(int, input().split())
    a = list(map(int, input().split()))
    
    lis = [[i-x, i+x] for i in a]
    l = lis[0][0]
    r = lis[0][1]
    ans = 0
    
    for i in range(n):
        l = max(lis[i][0],l)
        r = min(lis[i][1],r)
        
        if l > r:
            ans +=1
            l = lis[i][0]
            r = lis[i][1]
    
    print(ans)
    

