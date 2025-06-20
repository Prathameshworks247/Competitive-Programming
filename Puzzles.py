n,m = map(int, input().split())
f = list(map(int, input().split()))

f.sort()

miny = float("inf")
for i in range(n-1,len(f)):
    miny = min(miny, f[i]- f[i-3])
    
print(miny)
