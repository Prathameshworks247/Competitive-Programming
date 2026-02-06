T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Get sorted list of distinct values
    lis = sorted(set(a))
    
    # The maximum MEX we can achieve with k-1 elements is k-1
    # This happens when we have 0,1,2,...,k-2
    
    # Find MEX of the entire array first
    mex_val = 0
    for val in lis:
        if val == mex_val:
            mex_val += 1
        else:
            break
    
    # If MEX of array >= k, we can achieve MEX = k
    if mex_val >= k:
        print(k-1)
    else:
        # Otherwise, best we can do is the current MEX
        print(mex_val)
