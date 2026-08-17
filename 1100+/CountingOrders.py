t = int(input())
import math
import bisect
MOD = 10**9 + 7

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort(reverse=True)
    # print(a)
    # print(b)
    i = 0 
    j = 0
    result = 1
    for i in range(n):
    # Find the number of elements in a that are greater than b[i]
        temp = bisect.bisect_right(a, b[i])
        count = len(a) - temp
        result = result * max(count - i, 0) % MOD
	# Output the result for the current test case
    print(result)
