T = int(input())

for _ in range(T):
    n = int(input())
    s = input().strip()
    
    z = s.count("0")  
    mismatch = sum(1 for i in range(z) if s[i] == "1")
    print(mismatch)
