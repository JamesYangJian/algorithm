import os
import sys


def icurt(number, rnd):
    
    temp = float(number - 1)
    for i in range(0, rnd):
        temp = (2*temp + number/(temp**2)) / 3

    print 'Finished in %d rounds!' % (rnd)
    return temp


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: python %s number round' % (__file__)
        sys.exit(0)


    number = int(sys.argv[1])
    rnd = int(sys.argv[2])

    temp = icurt(number, rnd)


    print 'the cube root for %d is %.4f' % (number, temp)
