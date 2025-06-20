import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mn = min(a) 
    mx = max(a)
    
    if mn == mx:
        print("No")
    else:
        print("Yes")  # print the result - 1
        for i in range(n):
            if a[i] == mx:
                print(1,end=" ")
            else:
                print(2, end= " ")
        print()
    