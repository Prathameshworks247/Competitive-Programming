t = int(input())

for _ in range(t):
    s = list(input())
    n = len(s)
    
    mat = []
    for i in range(n):
        mat.append(s)
        s = s[:-1]  + s[:n-1]
        
    