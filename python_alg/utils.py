def check_num_in_bits(n):
    count = 0
    while n:
        # n = n&(n-1) can erase a 1 in least bit eg. 1101 ==> 1100 ==> 1000 ==> 0000
        n = n&(n-1)
        count += 1
        
    return count
    
def check_different_bits(a, b):
    count = 0
    
    # check the num of bits with value 1 for the XOR result of the two number
    c = a ^ b
    count = check_num_in_bits(c)
    
    return count
    
def generate_mask(n):
    mask = 0
    for i in range(n):
        mask |= 1<<i
        
    return mask
    
    
def check_num_power_of_2(a):
    import math
    n = int(math.log(a, 2))
    mask = generate_mask(n)
    
    if a == ((~a & mask) + 1):
        return True
    else:
        return False
        
def dfs_topsort(G):
    S, res = set(), []
    def recurse(u):
        if u in S:
            return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)
    for u in G:
        recurse(u)
    res.reverse()
    
    return res
    
    
def walk(G, s, S=set()):
    P, Q = {}, set()
    P[s] = None
    
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            Q.add(v)
            P[v] = u
            
    return P