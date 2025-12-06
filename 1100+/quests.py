# Import necessary modules
import sys

# Read the number of test cases
t = int(sys.stdin.readline().strip())

# Loop through each test case
for _ in range(t):
	# Read the number of quests and the maximum number of quests Monocarp can complete
	n, k = map(int, sys.stdin.readline().strip().split())

	# List to store experience points for first completion
	a = list(map(int, sys.stdin.readline().strip().split()))
	# List to store experience points for subsequent completions
	b = list(map(int, sys.stdin.readline().strip().split()))

	maxi = 0  # Variable to store the maximum experience points for subsequent completions
	sum = 0   # Variable to store the cumulative experience points
	ans = 0   # Variable to store the maximum possible total experience

	# Calculate the maximum possible total experience
	for i in range(min(n, k)):
		sum += a[i]  # Add the experience points for the first completion
		maxi = max(maxi, b[i])  # Update the maximum experience points for subsequent completions
		ans = max(ans, sum + (k - (i + 1)) * maxi)  # Calculate the maximum possible total experience

	# Output the result for the current test case
	print(ans)

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
