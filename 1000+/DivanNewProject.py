# t = int(input())


# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))

#     mapp = [[a[i],i+2] for i in range(n)]
    
#     mapp.sort(reverse=True)
#     # print(mapp)
#     mins = 0
#     ans = [1]
#     for i in range(n):
#         # print(ans)
#         if i %2 == 0:
#             ans = [mapp[i][1]] + ans
#         else:
#             ans.append(mapp[i][1])    
#         mins += mapp[i][0] * (i//2 + 1) * 2

#     print(mins)
#     print(" ".join(map(str, ans)))

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    buildings = [(a[i], i+1) for i in range(n)]  
    buildings.sort(reverse=True)  
    
    coords = [0] * (n+1)  
    total_time = 0
    cur_dist = 1  
    
    for i, (visits, idx) in enumerate(buildings):
        if i % 2 == 0:
            coords[idx] = cur_dist
        else:
            coords[idx] = -cur_dist
            cur_dist += 1
    
    for visits, idx in buildings:
        total_time += visits * abs(coords[idx]) * 2
    
    print(total_time)
    print(*coords)
