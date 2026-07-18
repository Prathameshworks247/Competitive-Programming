t = int(input())


# for _ in range(t):
#     n,k = map(int, input().split())
#     a = list(map(int,input().split()))
#     a.sort()
#     i = 0
#     j = 1
#     m = len(a)-1
#     print(a)
#     for l in range(k):
#         print(a[i:j+1],a[m], i,j)
#         if sum(a[i:j+1]) < a[m]:
#             i += 2
#             j += 2
#         else:
#             m -= 1
#     print(a[i:m+1])
#     print(sum(a[i:m+1]))

        
# Greedy is not the way here, Try Brute force
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int,input().split()))
    a.sort()
    pref = [0]
    for v in a:
        pref.append(v + pref[-1])
    ans = 0
    for x in range(k+1):
        l = 2*x
        r = n-(k-x)
        ans = max(ans, pref[r] - pref[l])
        
    print(ans)
        
        