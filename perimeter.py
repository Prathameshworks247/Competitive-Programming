t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    perimeter = (4 * m) * n  
    minus = [0, 0]  
    for i in range(n):
        x, y = map(int, input().split())
        minus[0] += x 
        minus[1] += y  
        
        perimeter -= abs(minus[0] - x) + abs(minus[1] - y)

    print(perimeter)