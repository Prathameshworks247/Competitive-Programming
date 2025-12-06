import sys
from bisect import bisect_left

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index])  # Number of test cases
index += 1

results = []

for _ in range(t):
	n = int(data[index])  # Length of the array
	index += 1

	v = []  # List to store array elements along with their indices

	# Read the array elements and store them with their indices
	for i in range(n):  # O(n)
		a = int(data[index])
		index += 1
		v.append((a, i))

	# Sort the list based on the array elements
	v.sort()  # O(nlogn)

	pre = [0] * n  # Prefix sum array

	# Calculate prefix sums
	pre[0] = v[0][0]
	for i in range(1, n):  # O(n)
		pre[i] = pre[i - 1] + v[i][0]

	ans = [0] * n  # To store the result for each element

	# Calculate the maximum number of additional elements that can be removed
	for i in range(n):  # O(nlogn)
		j = i
		found = i
		while j < n:
			temp = (pre[j] + 1, -float('inf'))
			idx = bisect_left(v, temp)
			idx -= 1
			if idx == j:
				break
			found += idx - j
			j = idx
		ans[v[i][1]] = found

	# Collect the results for the current test case
	results.append(' '.join(map(str, ans)))

# Output all results
sys.stdout.write('\n'.join(results) + '\n')

# Time Complexity (TC): O(nlogn)
# Space Complexity (SC): O(n)
