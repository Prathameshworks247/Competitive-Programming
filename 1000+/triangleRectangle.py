t = int(input())  # number of testcases

for _ in range(t):
    w, h = map(int, input().split())

    k1, *x_bottom = map(int, input().split())
    while len(x_bottom) < k1:
        x_bottom += list(map(int, input().split()))
    k2, *x_top = map(int, input().split())
    while len(x_top) < k2:
        x_top += list(map(int, input().split()))
    k3, *y_left = map(int, input().split())
    while len(y_left) < k3:
        y_left += list(map(int, input().split()))
    k4, *y_right = map(int, input().split())
    while len(y_right) < k4:
        y_right += list(map(int, input().split()))
    
    maxx = 0
    
    maxx = max(maxx, (max(x_bottom) - min(x_bottom))*h)
    maxx = max(maxx, (max(x_top) - min(x_top))*h)
    maxx = max(maxx, (max(y_left) - min(y_left))*w)
    maxx = max(maxx, (max(y_right) - min(y_right))*w)

    
    print(maxx)
    
    
    
    