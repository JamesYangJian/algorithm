

def find_sccs(G, s):
    """
    This version contains errors
    Since all nodes are in the path, in some cases, a scc will contain another independent scc
    Needs to be fixed
    """
    sccs = []
    cur_path = []
    Q = []

    Q.append(s)
    while Q:
        n = Q.pop()
        
        if G[n]:
            cur_path.append(n)

            for v in G[n]:
                if v in cur_path:
                    scc = set(cur_path[cur_path.index(v):cur_path.index(n)+1])
                    for v_scc in sccs:
                        if v_scc.intersection(scc):
                            v_scc.update(scc)
                            break
                    else:
                        sccs.append(scc)

                else:
                    Q.append(v)

    return sccs



def find_sccs_rec(G, s, cur_path=[], sccs=[]):
    """
    Use DFS to find scc in a graph
    traverse the graph in each path, find the SCC and put it into list
    remove node from path when all of its children has been handled
    """

    cur_path.append(s)

    for v in G[s]:
        if v in cur_path:
            scc = set(cur_path[cur_path.index(v):cur_path.index(s)+1])
            for v_scc in sccs:
                if v_scc.intersection(scc):
                    v_scc.update(scc)
                    break
            else:
                sccs.append(scc)
        else:
            cur_path.append(v)
            find_sccs_rec(G, v, cur_path, sccs)
            cur_path.pop()
    cur_path.pop()

    return sccs


if __name__ == '__main__':
    G = {
        'a': ['b', 'c'],
        'b': ['e', 'd'],
        'd': ['a'],
        'c': ['d'],
        'e': ['f'],
        'f': ['g'],
        'g': ['e', 'h'],
        'h': ['i'],
        'i': ['h', 'j'],
        'j':[]

    }


    for n in G:
        sccs = []
        print('start node: %s' % n)
        sccs = find_sccs_rec(G, n, cur_path=[], sccs=[])
        print(sccs)