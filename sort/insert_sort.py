import sys
import time
import random


def insert_sort(A, low, high):
    for i in xrange(low+1, high+1):
        v = A[i]
        idx = i-1
        while idx >= low and A[idx] > v:
            A[idx+1] = A[idx]
            idx -= 1
        A[idx+1] = v
                

if __name__ == '__main__':
    random.seed(time.time())
    print_list = False
    total_len = int(sys.argv[1])
    if (len(sys.argv) > 2) and sys.argv[2] == 'p':
        print_list = True

    A = []
    for i in xrange(0,total_len):
        A.append(random.randint(-100, 100))

    print 'Original Array'
    if print_list:
        print A
    t = time.time()
    
    insert_sort(A, 0, total_len-1)
    usage = time.time() -t
    print 'Sorted Array, usage=%f' %(usage)
    if print_list:
        print A

