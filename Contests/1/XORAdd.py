T = int(input())

for _ in range(T):
    a, b, x, y = map(int, input().split())
    
    if a == b:
        print(0)
        continue
    
    if (a == b + 1) and (a % 2 == 1):
        print(y)
        continue
    
    if b < a:
        print(-1)
        continue
    
    if x <= y:
        print((b - a) * x)
        continue

    ans = 0
    while a < b:
        if a % 2 == 0:
            a ^= 1
            ans += y
        else:
            a += 1
            ans += x
    print(ans)
