import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    a = []
    for i in range(n):
        a.append(int(data[index]))
        index += 1   
    unique_values = set()
    has_non_missing = False
    for val in a:
        if val != -1:
            has_non_missing = True
            unique_values.add(val)
    
    if not has_non_missing:
        print("YES")
    elif len(unique_values) == 1:
        v = next(iter(unique_values))
        if v >= 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
