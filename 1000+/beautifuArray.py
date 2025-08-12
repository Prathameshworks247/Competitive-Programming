t = int(input())
import math
for _ in range(t):
    n,k,b,s = map(int, input().split())

    ans = [0]*n
    
    ans[0] = k*b
    
    rem = s-k*b
    i = 0
    while s!=0 and i < n:
        if rem > k-1:
            rem -= k-1
            ans[i] += k-1
        else:
            ans[i] += rem
            break
        i += 1
    res = 0
    summ = 0
    for i in ans:
        res += math.floor(i/k)
        summ += i
    if res == b and summ == s:
        print(" ".join(map(str,sorted(ans))))
    else:
        print("-1")