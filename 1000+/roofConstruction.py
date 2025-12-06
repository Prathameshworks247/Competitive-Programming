import math
t = int(input())

for _ in range(t):
    n = int(input())

    msb = math.floor(math.log(n-1,2))
    
    for i in range(pow(2,msb)-1, -1,-1):
        print(i,end=" ")
    for i in range(pow(2,msb),n):
        print(i,end=" ")
    print()
