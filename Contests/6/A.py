T = int(input())


for _ in range(T):
    n = int(input())
    w = n
    count = w//2
    w = n//2 if n % 2 == 0 else n//2 + 1
    l = n//2
    
    while w > 1 or l > 1:
        count += (w//2 + l//2)
        l = l//2 if l % 2 == 0 else l//2 + 1
        l += w//2
        w = w//2 if w % 2 == 0 else w//2 + 1
    
    print(count+1)