T = int(input())

for _ in range(T):
    n = int(input())
    s = input()
    chars = set()
    temp1 = []
    temp2 = []
    for i in range(n):
        if s[i] not in chars:
            chars.add(s[i])
        temp1.append(len(chars))
    chars.clear()
    for i in range(n - 1, -1, -1):
        if s[i] not in chars:
            chars.add(s[i])
        temp2.append(len(chars))
    ans = 0
    temp2.reverse()
    # print(temp1)
    # print(temp2)
    for i in range(n - 1):
        ans = max(ans, temp1[i] + temp2[i+1])
    print(ans)