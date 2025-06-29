T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    temp = []
    ans = []
    for i in range(n):
        if a[i]%k == 0:
            temp.append((k, i))
        else:
            temp.append((a[i]%k,i))
    rev_sort = sorted(temp, key=lambda x: (-x[0], x[1]))
    # print(rev_sort)
    for i in range(n):
        ans.append(rev_sort[i][1]+1)
        
    print(' '.join(map(str, ans)))
    