import sys

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index]) # Number of test cases
index += 1

results = []

for _ in range(t):
	n = int(data[index]) # n: number of books in each stack
	x = int(data[index + 1]) # x: Tenzing's favorite number
	index += 2

	# Precomputed OR results for each stack
	pre = [[] for _ in range(3)]

	for i in range(3):
		s = 0 # Initialize current OR result
		pre[i].append(s) # Start with 0 OR result

		# Read each book's difficulty in the stack
		for j in range(n):
			a = int(data[index])
			index += 1

			# If adding this book changes the OR result, update it
			if (s | a) != s:
				s |= a
				pre[i].append(s)

	ans = False # Flag to check if x can be achieved

	# Check all combinations of OR results from the three stacks
	for A in pre[0]: # Iterate over precomputed OR results of stack 1
		for B in pre[1]: # Iterate over precomputed OR results of stack 2
			for C in pre[2]: # Iterate over precomputed OR results of stack 3
				# Check if the combined OR result equals x
				if (A | B | C) == x:
					ans = True

	# Store the result for the current test case
	results.append("YES" if ans else "NO")

# Output all results
sys.stdout.write("\n".join(results) + "\n")

# Time Complexity (TC): O(max(3*n, (31^3)))
# Space Complexity (SC): O(3*31)
