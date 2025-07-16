###################################
import math
T = int(input())

def lcm(a, b):
    lcm = a*b// math.gcd(a, b)
    return lcm
for _ in range(T):
    n = int(input())
    i = 1
    j = n-1
    min = 0
    while i<j:
        
        