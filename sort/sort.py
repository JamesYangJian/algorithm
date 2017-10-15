import sys
import random
import time


from heap_sort_class import *
from count_sort import *
from qsort import *
from merge_sort import *
from insert_sort import *



if __name__ == '__main__':
    random.seed(time.time())
    print_list = False
    total_len = int(sys.argv[1])
    method = sys.argv[2]
    range_min = int(sys.argv[3])
    range_max = int(sys.argv[4])

    if (len(sys.argv) > 5) and sys.argv[5] == 'p':
        print_list = True

    if method == 'count':
        range_min = 0

    A = []
    for i in xrange(0,total_len):
        A.append(random.randint(range_min, range_max))

    if print_list:
        print 'Original Array'
        print A
    t = time.time()

    print 'Start Sorting!'
   
    if method == 'heap':
        heap_sort(A)
    elif method == 'count':
        A = count_sort(A, range_max)
    elif method == 'quick':
        QSort(A, 0, total_len-1)
    elif method == 'merge':
        merge_sort(A, 0, total_len-1)
    elif method == 'insert':
        insert_sort(A, 0, total_len-1)

    #merge_sortion(A, 0, total_lendd-1)
    usage = time.time() -t
    print 'Sorted Array, usage=%f' %(usage)
    if print_list:
        print A
