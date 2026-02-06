T = int(input())

for _ in range(T):
    n = int(input())
    lis = list[int](range(1, n + 1))
    ans = []

    mid = (n - 1) // 2
    ans.append(lis[mid])

    step = 1
    while len(ans) < n:
        if mid + step < n:
            ans.append(lis[mid + step])
        if mid - step >= 0 and len(ans) < n:
            ans.append(lis[mid - step])
        step += 1

    print(" ".join(map(str, ans)))
