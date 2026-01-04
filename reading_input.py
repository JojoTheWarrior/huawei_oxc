from collections import deque
import indexing_functions

# N <= 32 (even), S <= 32, L <= 64, NSL <= 2^14 (groups * spines * leaves)
N, S, L = map(int, input().split())
M, K, P = map(int, input().split())

# setting global variables in indexing_functions.py
indexing_functions.set_params((N, S, L, M, K, P))

conv_ratio = M * K / (P * L)

# avail[P][gp1][gp2] contains a list of pairs of (spine1, spine2) that can connect gp1 to gp2
avail = [[[deque() for _ in range(N)]
            for _ in range(N)]
            for _ in range(N)]
# ports[P][gp][spine][OXC]
ports = [[[[-1 for _ in range(M)]
            for _ in range(S/P)]
            for _ in range(N)]
            for _ in range(P)]

for p in range(P):
    for gp1 in range(N):
        for gp2 in range(N):
            # fixed p, gp1, and gp2
            for a in range(0, S/P):
                for b in range(0, S/P):
                    avail[p][gp1][gp2].append((p*S/P + a, p*S/P+b))

for query_set in range(1, 5+1):
    plane_pointer = 0
    Q = int(input())

    all_qs = []
    for _ in range(Q):
        gA, lA, gB, lB = map(int, input().split())
        all_qs.append((gA, lA, gB, lB))

        # pick a plane
        p = plane_pointer
        plane_pointer = (plane_pointer+1) % P

        # pick a spine for (gA, lA)
        for sp1 in range(p*(S/P), (p+1)*(S/P)):
            # pick an OXC
            for oxc in range(0, M):
                if ports[p][gA][sp1][oxc] == -1:
                    pass
                else:
                    


