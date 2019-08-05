
def dfs_traverse(G, s, qtype=list):
    S = []
    Q = qtype()
    Q.append(s)
    result = []

    while Q:
        n = Q.pop()
        S.append(n)
        for t in G[n]:
            if t in S:
                continue
            Q.append(t)

        result.append(n)

    return result


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        depth = 3
    else:
        depth = int(sys.argv[1])

    G = {}

    max_node = 2 ** depth - 1

    max_leaf = 2**(depth+1) - 1

    for i in range(0, max_node):
        G[i] = [2*i+1, 2*i+2]

    for i in range(max_node, max_leaf):
        G[i] = []

    result = dfs_traverse(G, 0)

    print(result)






