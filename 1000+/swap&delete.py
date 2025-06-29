T = int(input())

for _ in range(T):
    s = input()
    ones = s.count('1')
    zeros = s.count('0')
    temp = ""
    ans = 0
    for i in s:
        if i == "1" and zeros> 0:
            temp += "0"
            zeros -= 1
        elif i == "0" and ones > 0:
            temp += "1"
            ones -= 1
        else:
            ans = len(s) - len(temp)
            break
    print(ans)
            
            