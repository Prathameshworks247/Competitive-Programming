def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        # If k == n*n - 1, it's impossible because one cell must be non-escapable
        if k == n * n - 1:
            print("NO")
            continue
        
        print("YES")
        # Initialize grid with 'R' (right) as default
        grid = [['R'] * n for _ in range(n)]
        
        if k == n * n:
            # If k == n*n, all cells must be escapable, set all to 'U'
            for i in range(n):
                for j in range(n):
                    grid[i][j] = 'U'
        else:
            # We need exactly k escapable cells, so n*n - k cells should be non-escapable
            non_escape = n * n - k
            escaped = 0
            
            # First, set the grid to create a cycle for non-escapable cells
            for i in range(n):
                for j in range(n):
                    if i < n - 1:
                        grid[i][j] = 'D'  # Point down
                    else:
                        grid[i][j] = 'R'  # Last row points right
            
            # Adjust the grid to make exactly k cells escapable
            # Start from the bottom-right corner
            for j in range(n - 1, -1, -1):
                if escaped < k:
                    grid[n - 1][j] = 'U'  # Point up to escape
                    escaped += 1
                else:
                    grid[n - 1][j] = 'R'  # Point right to stay in cycle
            
            for i in range(n - 2, -1, -1):
                if escaped < k:
                    grid[i][n - 1] = 'U'  # Point up to escape
                    escaped += 1
                else:
                    grid[i][n - 1] = 'D'  # Point down to stay in cycle
        
        # Print the grid
        for row in grid:
            print(''.join(row))

solve()