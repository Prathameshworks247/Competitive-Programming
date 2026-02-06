t = int(input())

for _ in range(t):
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    h = 0
    while x > 0:
        if sum(a) == 0:
            if x > n:
                h += x // n
                x %= n
            else:
                break
        for i in range(n):
            if a[i] == 0:
                x -= 1
                continue
            a[i] -= 1
            #print(a)
        h += 1
    print(h if h == 2 else (h-1))            
    