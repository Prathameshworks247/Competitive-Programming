import math
###############################
T = int(input())
for _ in range(T):
    n = int(input())
    px, py, qx, qy = map(int, input().split())
    a = list(map(int, input().split()))
    
    dist = math.sqrt((px - qx) ** 2 + (py - qy) ** 2)
    total_sum = sum(a)
    
    if total_sum < dist:
        print("No")
        continue
    
    if abs(total_sum - dist) < 1e-9:
        print("Yes")
        continue
    
    possible = True
    for i in range(n):
        if dist + total_sum < 2 * a[i]:
            possible = False
            break
    
    if possible:
        print("Yes")
    else:
        print("No")