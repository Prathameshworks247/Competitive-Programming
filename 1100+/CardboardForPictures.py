import math
t = int(input())

for _ in range(t):
    n,c = map(int, input().split())
    s = list(map(int, input().split()))

    l = 0 
    r = int(math.sqrt(c))
    while l <= r:
        mid = (l+r)//2
        summ = 0
        for i in s:
            summ += (i + 2*mid)**2
        if summ < c:
            l = mid+1
        else:
            r = mid - 1
    print(l)
    
# Binary search for width w.
# For each mid, compute total area = Σ((s[i] + 2*mid)^2).
# If total area < c, increase w; otherwise, decrease w.

