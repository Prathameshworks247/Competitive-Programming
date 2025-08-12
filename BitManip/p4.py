# Python3 program for the above approach

# Function to print the submasks of N
def SubMasks(N) :
    S = N 
    while S > 0:
        print(S,end=' ')
        S = (S - 1) & N

# Driven Code
if __name__ == '__main__':
    N = 25
    SubMasks(N)
    
    # This code is contributed by bgangwar59.