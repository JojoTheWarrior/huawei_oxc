from collections import deque
import indexing_functions
from indexing_functions import get_port, unpack_port
import random

# N <= 32 (even), S <= 32, L <= 64, NSL <= 2^14 (groups * spines * leaves)
N, S, L = map(int, input().split())
M, K, P = map(int, input().split())
R = N*(S//P)*K

# setting global variables in indexing_functions.py
indexing_functions.set_params((N, S, L, M, K, P))

conv_ratio = M * K / (P * L)

# avail[P][gp1][gp2] contains a list of pairs of (spine1, spine2) that can connect gp1 to gp2
avail = [[[deque() for _ in range(N)]
            for _ in range(N)]
            for _ in range(N)]
# ports[P][gp][spine][OXC] is -1 if unconnected, or (partner, degree) if connected
ports = [[[[-1 for _ in range(M)]
            for _ in range(S//P)]
            for _ in range(N)]
            for _ in range(P)]
# port_conns[oxc][port_num1] returns which other port port_num1 is connected to
# TODO: add another tracker counting the frequency of traversals across this port link

for p in range(P):
    for gp1 in range(N):
        for gp2 in range(N):
            # fixed p, gp1, and gp2
            for a in range(0, S//P):
                for b in range(0, S//P):
                    avail[p][gp1][gp2].append((p*S//P + a, p*S//P+b))

for query_set in range(1, 5+1):
    # try resetting port connections between all query sets
    port_conns = [[-1 for _ in range(R)]
                    for _ in range(M)]

    plane_pointer = 0
    Q = int(input())

    all_qs = []
    ans = []

    for _ in range(Q):
        gA, lA, gB, lB = map(int, input().split())
        all_qs.append((gA, lA, gB, lB))

        # pick a plane
        p = plane_pointer
        plane_pointer = (plane_pointer+1) % P

        flag = False

        while not flag:
            # pick an OXC at random
            oxc = random.randint(0, M-1)

            # pick a spine for (gA, lA)
            for sp1 in range(p*(S//P), (p+1)*(S//P)):
                port1 = get_port(gA, sp1, 0)
                if port_conns[oxc][port1] == -1:
                    # this one hasn't been connected yet
                    for sp2 in range(p*(S//P), (p+1)*(S//P)):
                        port2 = get_port(gB, sp2, 0)
                        if port_conns[oxc][port2] == -1:
                            port_conns[oxc][port1] = port2
                            port_conns[oxc][port2] = port1
                            ans.append([sp1, 0, oxc, sp2, 0])
                            flag = True
                            break
                else:
                    port2 = port_conns[oxc][port1]
                    # this one's already taken
                    gp2, sp2, lnk2 = unpack_port(oxc, port2)
                    # miraculously, the other connected port is of the same group
                    if gp2 == gB:
                        ans.append([sp1, 0, oxc, sp2, 0])
                        flag = True

                # if this sp1 worked
                if flag:
                    break

    # after all queries are done
    for oxc in range(M):
        print(*port_conns[oxc])
    
    for x in ans:
        print(*x)



