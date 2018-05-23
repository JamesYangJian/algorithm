import time
import random
import sys


def find_gcd(a, b):
    s, y = (a,b) if a > b else (b, a)
    gcd = y
    while gcd:
        y = gcd
        gcd = s % y
        s = y

    return y 


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: python __file__ range, number'
        sys.exit(0)

    r = int(sys.argv[1])
    number = int(sys.argv[2])

    random.seed(time.time())
    data_set = set()

    for i in range(0, number):
        data_set.add(random.randint(1, r))

    data_list = list(data_set)
    data_list = [1008,1260,882,1134]

    l = len(data_list)

    print data_list

    gcd = sys.maxint

    for i in range(0, l):
        for j in range(i+1, l):
            ret = find_gcd(data_list[i], data_list[j])
            gcd = ret if gcd > ret else gcd

    print 'gcd is %d' % (gcd)
