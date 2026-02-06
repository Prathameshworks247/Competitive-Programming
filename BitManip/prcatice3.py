def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Check if all elements are already 0
    if all(x == 0 for x in a):
        print(*range(1, n + 1))
        return
    
    valid_k = []
    
    # k = 1 always works
    valid_k.append(1)
    
    # Check other values of k
    for k in range(2, n + 1):
        if n % k == 0:
            valid_k.append(k)
    
    print(*valid_k)


t = int(input())
for _ in range(t):
    solve()