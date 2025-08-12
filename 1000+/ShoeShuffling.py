from collections import defaultdict
t = int(input())

def rotate_range(arr, first, middle, last):
    arr[first:last] = arr[middle:last] + arr[first:middle]
    return arr

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    students = [i+1 for i in range(n) ]
    doable = True
    dic = defaultdict(int)
    for i in s:
        dic[i] += 1
        
    for val in dic.values():
        if val < 2:
            doable = False
            break
    if doable:
        l = r =0
        while r < n:
            if s[l] == s[r]:
                r += 1
            else:
                students = rotate_range(students, l, l+1, r)      
                l = r   
        students = rotate_range(students, l, l+1, r)       
        print(" ".join(map(str, students)))
    else:
        print("-1")
        continue