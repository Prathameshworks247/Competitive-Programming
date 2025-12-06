import math
t = int(input())

for _ in range(t):
    n,r,b = map(int, input().split())
    
    ans = ""
    
    # print(reds_between)
    while r > 0 :
        reds_between = math.ceil(r/(b+1))
        if r > reds_between:
            
            ans+= reds_between*"R"
            ans += "B"
            b -= 1
            r -= reds_between
        else:
            ans += "R"*r
            b -= 1
            r -= reds_between
    print(ans)        
        
        
    