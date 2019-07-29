# -*- encoding: utf-8 -*-
"""
Find a star from a crowd
Star is: he knows nobody else in the crowd while anybody else knows him

Such as:

  0  1  1  0  0  0  1  0  0  1
  0  0  0  0  1  1  1  0  1  1
  0  0  1  1  1  0  0  0  1  1
  0  0  1  1  0  1  1  0  1  1
  1  0  1  1  1  1  0  0  1  1
  0  1  0  1  1  1  1  1  1  1
  0  1  1  1  1  0  0  0  0  1
  1  0  1  1  0  0  0  0  0  1
  1  1  1  1  0  0  0  1  0  1
  0  0  0  0  0  0  0  0  0  0

#9 is a star

Analyze: 
1. The most ordinary solution is a nxn check
2. This solution is to has a length n check to find a possible candidate, and use another length n check to confirm it

"""
def find_star(G):
    s = 0
    v = 1

    for c in range(2, len(G)+1):
        if c == len(G):
            print('Last round!')
        if s == c:
            continue

        if G[s][v] == 1:
            # if s knows v, then s isn't a star
            s = c
        elif G[v][s] == 1:
            # s doesn't know v, and v knows s, v won't be a star
            v = c
        else:
            # s doesn't know v, and v does'n know s, s, v both won't be star
            s = c
            # v = c+1

    if s == len(G):
        s = v


    print("Assume Start is #(%d)" % s)

    found = True
    for c in range(len(G)):
        if s == c:
            continue
        elif G[s][c] == 1:
            found = False
            break
        elif G[c][s] == 0:
            found = False
            break
    else:
        print("Found Star, he is #(%d)!!" % s)
        return s

    print("Ouch, no start found in this crowd!!")
    return None

        


if __name__ == '__main__':
    import random

    total = 100

    G = [[random.randrange(2) for i in range(total)] for i in range(total)]

    s = random.randrange(total)
    # s = total - 1
    print('Pre Set Star is #(%d)' % s)

    for i in range(total):
        G[i][s] = 1
        G[s][i] = 0

    # for row in G:
    #     print(" %2i" * total % tuple(row))

    find_star(G)