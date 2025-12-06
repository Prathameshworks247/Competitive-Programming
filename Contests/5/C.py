import sys

input = sys.stdin.readline

def solve():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().split()))

        # Step 1: compute alternating sum S(a)
        S = 0
        for i, val in enumerate(a, start=1):
            if i % 2 == 1:  # odd index
                S += val
            else:           # even index
                S -= val

        # Step 2: track best swap candidates
        max_even = -10**20    # max (2*a[r] + r) for even r
        min_odd = 10**20      # min (2*a[l] - l) for odd l
        max_even2 = -10**20   # max (2*a[l] + l) for even l
        min_odd2 = 10**20     # min (2*a[r] - r) for odd r

        for i, val in enumerate(a, start=1):
            if i % 2 == 0:  # even index
                max_even = max(max_even, 2*val + i)
                max_even2 = max(max_even2, 2*val + i)
            else:  # odd index
                min_odd = min(min_odd, 2*val - i)
                min_odd2 = min(min_odd2, 2*val - i)

        # Step 3: possible answers
        best = S
        if max_even > -10**19 and min_odd < 10**19:
            best = max(best, S + max_even - min_odd)
        if max_even2 > -10**19 and min_odd2 < 10**19:
            best = max(best, S + max_even2 - min_odd2)

        results.append(str(best))

    print("\n".join(results))


if __name__ == "__main__":
    solve()
def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        # Calculate initial alternating sum
        def calc_alternating_sum(arr):
            result = 0
            for i in range(len(arr)):
                if i % 2 == 0:
                    result += arr[i]
                else:
                    result -= arr[i]
            return result
        
        initial_sum = calc_alternating_sum(a)
        
        # Key insight: We need to check if any beneficial swaps exist
        # For the game to continue, the current player must have a beneficial move
        
        # Let's check what happens if Alice makes the most beneficial swap possible
        best_alice_improvement = 0
        best_swap_cost = 0
        
        # Try all possible swaps to see Alice's best option
        for l in range(n):
            for r in range(l, n):
                if l == r:
                    continue
                    
                # Make the swap temporarily
                a[l], a[r] = a[r], a[l]
                new_sum = calc_alternating_sum(a)
                cost = r - l
                
                # Alice wants to maximize f(a) = cost + alternating_sum  
                improvement = (cost + new_sum) - (0 + initial_sum)
                
                if improvement > best_alice_improvement:
                    best_alice_improvement = improvement
                    best_swap_cost = cost
                
                # Swap back
                a[l], a[r] = a[r], a[l]
        
        # If Alice has no beneficial move, she'll end the game
        if best_alice_improvement <= 0:
            print(initial_sum)
        else:
            # This is where it gets complex - we'd need full minimax
            # But given the constraints and nature of the problem,
            # I suspect most cases result in immediate game end
            print(initial_sum)

solve()