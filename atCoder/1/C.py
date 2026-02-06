import math

def count_pairs(n):
    count = 0
    max_x = int(math.sqrt(n / 2)) + 1
    
    for x in range(1, max_x + 1):
        remainder = n - x * x
        if remainder <= 0:
            break
        
        y = int(math.sqrt(remainder))
        if y * y == remainder and y > x:
            count += 1
    
    return count

def find_good_integers(N):
    good_integers = []
    
    for n in range(1, N + 1):
        if count_pairs(n) == 1:
            good_integers.append(n)
    
    return good_integers

N = int(input())

good_integers = find_good_integers(N)

k = len(good_integers)
print(k)
if k > 0:
    print(' '.join(map(str, good_integers)))
else:
    print()