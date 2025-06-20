from collections import Counter

n,k = map(int,input().split())
i = list(input())

a = Counter(i)
sorted_by_keys = dict(reversed(sorted(a.items(), key=lambda item: item[1])))
l = []
m = k
first_value = next(iter(a.values())) 

if first_value >= k:
        l = [k]
else:
    for key,value in sorted_by_keys.items():
        if value < m:
            l.append(value)
            m -= value
        elif value >= m:
            l.append(m)
            break

ans = 0

for i in l:
    ans += i**2
print(ans)
    