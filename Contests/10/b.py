t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    c0 = s.count('0')
    c1 = n - c0

    diff = c0 - c1

    # Deleted characters can alternate only if their counts
    # differ by at most 1. Since the kept alternating string
    # has count difference at most 1, |c0 - c1| must be <= 2.
    if abs(diff) > 2:
        print(-1)
        continue

    def longest_alternating(start):
        expected = start
        length = 0

        for ch in s:
            if int(ch) == expected:
                length += 1
                expected ^= 1

        return length

    L0 = longest_alternating(0)
    L1 = longest_alternating(1)

    best = 0

    # Case 1: kept string has equal number of 0s and 1s
    # => its length must be even.
    # r0 - r1 = 0
    if abs(diff - 0) <= 1:
        best = max(
            best,
            L0 if L0 % 2 == 0 else L0 - 1,
            L1 if L1 % 2 == 0 else L1 - 1
        )

    # Case 2: kept string has one more 0 than 1
    # => odd length, starts with 0.
    # r0 - r1 = 1
    if abs(diff - 1) <= 1:
        best = max(
            best,
            L0 if L0 % 2 == 1 else L0 - 1
        )

    # Case 3: kept string has one more 1 than 0
    # => odd length, starts with 1.
    # r0 - r1 = -1
    if abs(diff + 1) <= 1:
        best = max(
            best,
            L1 if L1 % 2 == 1 else L1 - 1
        )

    print(n - best)