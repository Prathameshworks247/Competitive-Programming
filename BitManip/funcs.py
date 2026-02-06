x = 0b010010001000
n = len(bin(x)) - 2

a = x.bit_count()
b = (x&-x).bit_length() - 1 
c = n - x.bit_length()

print(a,b,c)

