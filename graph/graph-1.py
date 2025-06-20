n, t = map(int, input().split())
a = list(map(int, input().split()))

i = 0
visited_positions = set()

while i < n - 1:
    if i in visited_positions:  # Prevent infinite loops
        break
    visited_positions.add(i)
    
    i += a[i]  # Move to the next position
    
    if i == t - 1:  # Check if we reached the target
        print("YES")
        exit()

print("NO")
