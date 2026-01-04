from collections import deque

# N <= 32 (even), S <= 32, L <= 64, NSL <= 2^14 (groups * spines * leaves)
N, S, L = map(int, input().split())
M, K, P = map(int, input().split())

conv_ratio = M * K / (P * L)

# avail[P][gp1][gp2] contains a list of pairs of 
avail = [[[]]]

for query_set in range(1, 5+1):
    plane_pointer = 0
    Q = int(input())

    all_qs = []
    for _ in range(Q):
        gA, lA, gB, lB = map(int, input().split())
        all_qs.append((gA, lA, gB, lB))

    qs = {}
    for _ in range(Q):
        gA, lA, gB, lB = map(int, input().split())
        pA, pB = (gA, lA), (gB, lB)
        didSwap = False
        if pA > pB:
            pA, pB = pB, pA # swap them
            didSwap = True
        qs[(pA, pB)] = qs.get((pA, pB), 0) + 1
    
    plane_pointer = 0
    # answering queries
    for query, freq in qs:
