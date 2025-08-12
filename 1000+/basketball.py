# import math
# N,D = map(int,input().split())
# P = list(map(int,input().split()))

# P.sort(reverse=True)
# limit = N
# count = 0
# for i in range(N):
#     sub = math.ceil(D/P[i])
#     if sub <= N and P[i]*sub > D:
#         count += 1
#         N -= sub
# print(count)


N,D = map(int,input().split())
P = list(map(int,input().split()))
P.sort()
l = -1
r= N-1
count = 0
teamsize = 1

while l < r:
    if P[r] * teamsize <= D and l<r:
        l += 1
        teamsize += 1
    else:
        r-= 1
        teamsize = 1
        count +=1 
print(count) 