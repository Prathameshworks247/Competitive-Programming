a = list(map(int, input().split()))

i = 0 
j = 1

summ = 0

while j < len(a):
    summ += a[i] ^ a[j]