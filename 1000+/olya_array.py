T = int(input())

for _ in range(T):
    n  = int(input())
    dump = []
    dump2 = []
    for _ in range(n):
        m = int(input())
        temp = list(map(int, input().split()))
        temp.sort()
        dump.append(temp[0])
        dump2.append(temp[1])
    second_min  = min(dump2)
    ans = (sum(dump2) - second_min) + min(dump)
    print(ans)