import math
import sys
import copy
import time


"""
This program use different ways to caculate Pascal(YangHui) Triangles
0. Pascal triangle is acutally the cofficient of binomial distribution
1. use two arrays to add each other with 1 shift
2. use one array, iterate it and add element n and n+1, each time head-add zero
3. use one array, iterate it and add element n and n+1, each time tail-add zero
"""

def binomial_coff(m, n):
    coff = math.factorial(m)/(math.factorial(n) * math.factorial(m-n))
    return coff


if __name__ == '__main__':
    count = int(sys.argv[1])
    idx = int(sys.argv[2])
    coff = [1]
    #print coff
    
    if idx == 0:
        print '-----------------solution 0--------------'
        s = time.time()
        for i in range(1, count):
            coff = []
            for j in range(0, i+1):
                coff.append(binomial_coff(i, j))
            #print coff
        usage = time.time() -s
        print 'usage:%f' % (usage)
        
    if idx == 0 or idx == 1:
        print '-----------------solution 1--------------'
        s = time.time()
        a = [1]
        #print a
        for c in range(1, count):
            b = copy.deepcopy(a)
            a.insert(len(a), 0)
            b.insert(0, 0)
            a = list(a[i]+b[i] for i in range(0, len(a)))
            #print a

        usage = time.time() -s
        print 'usage:%f' % (usage)

    if idx == 0 or idx == 1 or idx == 2:
        print '-----------------solution 2--------------'
        s = time.time()
        a = [1]
        #print a

        for c in range(1, count):
            a.insert(0, 0)
            for i in range(0, c):
                a[i] = a[i] + a[i+1]
            #print a
        usage = time.time() -s
        print 'usage:%f' % (usage)

    if idx == 0 or idx == 1 or idx == 2 or idx == 3:
        print '-----------------solution 3--------------'
        s = time.time()
        a = [1]
        #print a

        for c in range(0, count):
            a.insert(len(a), 0)
            for i in range(c+1, 0, -1):
                a[i] = a[i] + a[i-1]
            #print a
        usage = time.time()-s
        print 'usage:%f' % (usage)
        
