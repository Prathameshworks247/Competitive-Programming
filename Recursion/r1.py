# def recur(i,n):
#     if i == n :
#         print(i)
#         return
#     print(i)
#     recur(i+1,n)
    

# recur(1,10)

# def recur(i,n):
#     if i == n :
#         print(i)
#         return
    
#     recur(i+1,n)
#     print(i)

# recur(1,10)

#Factorial of a number

def factorial(n:int):
    if n == 1:
        return 1
    ans = n * factorial(n-1)
    return ans

print(factorial())