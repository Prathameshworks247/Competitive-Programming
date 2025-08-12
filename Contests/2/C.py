T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Get unique heights in sorted order
    unique_heights = sorted(set(a))
    
    # Find position of starting tower's height
    start_height = a[k-1]
    start_pos = unique_heights.index(start_height)
    
    # Current time and position
    current_time = 0
    current_pos = start_pos
    
    # Try to move to each higher tower
    can_survive = True
    
    while current_pos + 1 < len(unique_heights):
        current_height = unique_heights[current_pos]
        next_height = unique_heights[current_pos + 1]
        
        # Time when we must leave current tower (before water level exceeds height)
        must_leave_by = current_height - current_time
        
        # Time needed to teleport to next tower
        teleport_time = abs(next_height - current_height)
        
        # Check if we can make the teleport
        if must_leave_by < teleport_time:
            can_survive = False
            break
        
        # Update time and position
        current_time += teleport_time
        current_pos += 1
    
    if can_survive:
        print("YES")
    else:
        print("NO")

# T = int(input())

# for _ in range(T):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     aa = list(set(sorted(a)))
#     for i in range(len(aa)):
#         if aa[i] == a[k-1]:
#             posi = i

#     flag = False
#     k_h = aa[posi]
#     w_h = 1
#     while posi+1 < len(aa):
#         diff = aa[posi] - w_h
#         if diff+1 >= aa[posi+1] - aa[posi]:
#             posi += 1
#             w_h+=1
#         else:
#             flag = True
#             break
#     if flag:
#         print("NO")
#     else:
#         print("YES")