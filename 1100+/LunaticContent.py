import math
t = int(input())


for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    ans = 0
    for i in range(n):
        
        ans = math.gcd(ans, abs(a[i] - a[n-i-1]))
        
    print(ans)