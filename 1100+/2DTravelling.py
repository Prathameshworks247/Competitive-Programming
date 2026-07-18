t = int(input())

def dist(a,b):
    return (abs(cities[a-1][0] - cities[b-1][0]) + abs(cities[a-1][1] - cities[b-1][1]))

for _ in range(t):
    n,k,a,b = map(int,input().split())
    cities = [tuple(map(int, input().split())) for _ in range(n)]
    major_cities = cities[:k]
    if a <= k and b <=k:
        print(0)
        continue
    temp_dist1 = dist(a,b)
    min_from_a = float('inf')
    min_from_b = float('inf')
    for i in range(k):
        min_from_a = min(min_from_a, dist(a,i+1))
    for i in range(k):
        min_from_b = min(min_from_b, dist(b,i+1))
    
    print(min(temp_dist1, (min_from_a + min_from_b)))

# Compare:
# 1. Direct distance from a to b
# 2. Distance from a to nearest major city + distance from b to nearest major city
#    (0 if a or b is already a major city)

    