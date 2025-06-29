from collections import defaultdict

T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c_a = defaultdict(int)
    c_b = defaultdict(int)
    
    count = 1
    for i in range(1,n):
        if a[i - 1] == a[i]:
            count += 1
        else:
            c_a[a[i-1]] = max(count, c_a[a[i-1]])
            count = 1
    c_a[a[-1]] = max(c_a[a[-1]], count) 
    count = 1
    for j in range(1,n):
        if b[j - 1] == b[j]:
            count += 1
        else:
            c_b[b[j-1]] = max(count, c_b[b[j-1]])
            count = 1
    c_b[b[-1]] = max(c_b[b[-1]], count)
             
    all_keys = set(c_a.keys()).union(set(c_b.keys()))
    max_streak = 0
    for k in all_keys:
        total = c_a[k] + c_b[k]
        max_streak = max(max_streak, total)

    print(max_streak)
