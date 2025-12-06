t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    w = s.count("W", 0, k)
    ans = w
    i = 0
    j = k
    while j < n:
        if s[i] == "W":
            w -= 1
        if s[j] == "W":
            w += 1
        
        ans = min(ans, w)
        i += 1
        j += 1   
    print(ans)
