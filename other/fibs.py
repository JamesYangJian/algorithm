#!/usr/bin/python
import sys
import time
import numpy as np


def fibs_matrix(n):
    aa = np.array([[1,1],[1,0]], dtype=np.longdouble)
    bb = np.array([[1,1],[1,0]])
    

    if n == 0:
        return aa[1][1]
    elif n == 1:
        return aa[1][0]
    else:
        for i in xrange(0, num-1):
            aa = aa.dot(bb)
        return aa[1][0]

def fibs_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibs_recursive(n-1) + fibs_recursive(n-2)

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a

    def __iter__(self):
        return self


def fibs_iterate(n):
    if n == 0:
        return 0
    else:
        fibs = Fibs()
        for i in xrange(0, num):
            val = fibs.next()

        return val


if __name__ == '__main__':
    num = int(sys.argv[1])
    type = sys.argv[2]

    start = time.time()

    if type == 'r':
        sys.setrecursionlimit(100000)
        val = fibs_recursive(num)
    elif type == 'i':
        val = fibs_iterate(num)
    elif type == 'm':
        val = fibs_matrix(num)
    else:
        print 'unknows algorithm type:%s' % (type)

    end = time.time()
    usage = end - start
    
    print '[Type:%s, Usage:%f]The %d num of fibs is %d' % (type, usage, num, val,)
