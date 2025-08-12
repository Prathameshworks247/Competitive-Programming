T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    i = 0
    count = 0
    
    while i <= n - k:
        if all(a[j] == 0 for j in range(i, i + k)):
            count += 1
            i += k + 1  
        else:
            i += 1  
    print(count)
