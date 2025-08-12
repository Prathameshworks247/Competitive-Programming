T = int(input())
for _ in range(T):
    n, c = input().split()
    n = int(n)
    s = input()

    if c == 'g':
        print(0)
        continue

    s += s  
    max_dist = 0
    last_g = -1
    
    j = len(s) - 1
    
    while j >=0:
        if s[j] == 'g':
            last_g = j
        elif s[j] == c:
            max_dist = max(last_g - j , max_dist)
        j -= 1
    print(max_dist)

        
    
    