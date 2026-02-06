t=int(input())

for _ in range(t):
    n,q = map(int, input().split())
    a = list(map(int,input().split()))
    x = list(map(int,input().split()))
    pre = 31
    for xi in x:
        if xi >= pre:
            continue
        div = 2 ** xi
        for i in range(n):
            if a[i] % div == 0:
                a[i] += (div//2)
        pre = xi
    print(" ".join(list(map(str,a))))
            
    



    
