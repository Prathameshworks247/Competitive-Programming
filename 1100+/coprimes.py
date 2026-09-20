import sys
from math import gcd
pairs = [[] for _ in range(1001)]

input = sys.stdin.readline
for i in range(1, 1001):
	for j in range(1, 1001):
		if gcd(i, j) == 1:
			pairs[i].append(j)  # Store j as a coprime of i
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = -1
    # Array to store the index of each number in the array
    idx = [0]*1001

    for i,x in enumerate(a,1):
        idx[x] = i
    for i in range(1,1001):
        if idx[i] == 0:
            continue
            
        for j in pairs[i]:
            if idx[j] != 0:
                ans = max(ans, idx[i] + idx[j])
    print(ans)