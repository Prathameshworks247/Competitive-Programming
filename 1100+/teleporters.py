import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,c = map(int, input().split())
    a = list(map(int, input().split()))
    temp = []
    for i in range(n):
        temp.append(a[i] + i + 1)
    temp.sort()
    
    count = 0 
    i = 0
    while i < n and c >= temp[i]:
        c -= temp[i]
        i += 1
        count += 1
    
    print(count)