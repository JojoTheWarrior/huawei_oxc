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
    return i*K*S/P + j%(S/P)*K + k
    