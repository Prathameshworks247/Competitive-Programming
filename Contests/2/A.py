T = int(input())

for _ in range(T):
    x = input()
    minn = float("inf")
    
    for i in x:
        minn = min(minn, int(i))
    print(minn)
