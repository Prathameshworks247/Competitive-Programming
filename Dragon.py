# Input parsing
s, n = map(int, input().split())
dragons = [tuple(map(int, input().split())) for _ in range(n)]

# Sort dragons by their strength
dragons.sort()

# Simulate the battles
for x, y in dragons:
    if s > x:  # Kirito defeats the dragon
        s += y
    else:  # Kirito loses
        print("NO")
        break
else:
    print("YES")
