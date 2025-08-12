def solve_with_lookahead():
    n, k = map(int, input().split())
    casinos = []
    
    for i in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))
    
    memo = {}
    
    def max_coins(current_coins, visited_mask):
        if visited_mask in memo and current_coins in memo[visited_mask]:
            return memo[visited_mask][current_coins]
        
        if visited_mask not in memo:
            memo[visited_mask] = {}
        
        best = current_coins
        
        for i in range(n):
            if visited_mask & (1 << i): 
                continue
                
            l, r, real = casinos[i]
            if l <= current_coins <= r:
                new_mask = visited_mask | (1 << i)
                result = max_coins(real, new_mask)
                best = max(best, result)
        
        memo[visited_mask][current_coins] = best
        return best
    
    return max_coins(k, 0)

def solve():
    n, k = map(int, input().split())
    casinos = []
    
    for i in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))
    
    current_coins = k
    visited = [False] * n
    
    # Keep making moves until no improvement possible
    while True:
        best_casino = -1
        best_value = current_coins
        
        # Find the best casino we can currently visit
        for i in range(n):
            if visited[i]:
                continue
                
            l, r, real = casinos[i]
            
            # Check if we can visit this casino and it gives us more coins
            if l <= current_coins <= r and real > best_value:
                best_value = real
                best_casino = i
        
        # If no improvement possible, break
        if best_casino == -1:
            break
            
        # Visit the best casino
        visited[best_casino] = True
        current_coins = best_value
    
    return current_coins

# Test with simple greedy approach first
T = int(input())

for _ in range(T):
    print(solve())

# print(solve_with_lookahead())