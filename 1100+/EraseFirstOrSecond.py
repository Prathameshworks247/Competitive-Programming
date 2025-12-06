# T  = int(input())

# for _ in range(T):
    
#     n = int(input())
#     s = input()
#     ans = set()
#     def func(s:str):
#         if s in ans or len(s) == 0:
#             return
#         else:
#             ans.add(s)
#             # print(ans)
#         func(s[1:])
#         if len(s) > 2:
#             func(s[0]+s[2:])
#         else:
#             func(s[0])
#     func(s)
#     print(len(ans))
        
        
T = int(input())

for _ in range(T):
    n = int(input())
    s = input()
    a = set()
    ans= 0
    for i in range(n):
        a.add(s[i])
        ans += len(a)
    print(ans)



