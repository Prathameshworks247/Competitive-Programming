t = int(input())

for _ in range(t):
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    i = 0 
    j = 1
    count = 0
    while j < n:
        if abs((a[i] - a[j])//2) <= x:
            j += 1
            i+=1
        else:
            count +=1
            i += 1
            j += 1
    print(count)