N, S, L, M, K, P = (None,) * 6

def set_params(pms):
    global N, S, L, M, K, P
    N, S, L, M, K, P = pms

def get_port(i, j, k):
    """
    For a given OXC, group, spine, and link, returns the corresponding port number.
    
    :param i: Group number
    :param j: Spine number
    :param k: Link number
    """
    return int(i*K*S/P + j%(S/P)*K + k)

def unpack_port(m, i):
    """
    Returns (group, spine, link)
    
    :param m: OXC number
    :param i: Port number
    """
    gp = i // (K*S/P)
    sp = (i % ((S/P)*K)) // K + (m // (M/P)) * (S/P)
    lnk = i % K
    return tuple(map(int, (gp, sp, lnk)))
    