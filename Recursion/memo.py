memo = {}
def fibo(n:int):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(100000))