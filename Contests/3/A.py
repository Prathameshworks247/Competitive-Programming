def mex(T):
    for i in range(len(T)+1):
        if i not in T:
            return i
    
T=  int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    score = 0
    for i in range(n):
        for j in range(i+1, n):
            score += max(sum(a[i:j+1]),mex(a[i:j+1]))
            a = a[:i] + a[j+1:]
    print(score)