import sys
import random
import time


from heap_sort_class import *



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
    
    heap_sort(A)

    #merge_sortion(A, 0, total_lendd-1)
    usage = time.time() -t
    print 'Sorted Array, usage=%f' %(usage)
    if print_list:
        print A
