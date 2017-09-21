import sys
import random
import time


def merge(A, left, mid, right):
    array_len = right - left +1
    left_idx = 0
    right_idx = 0

    left_array=A[left:mid+1]
    left_array.append(sys.maxint)
    right_array=A[mid+1: right+1]
    right_array.append(sys.maxint)

    for i in xrange(left, right+1):
        # print 'left_idx= %d, left_len=%d'%(left_idx, len(left_array))
        # print 'right_idx= %d, right_len=%d'%(right_idx, len(right_array))
        if left_array[left_idx] < right_array[right_idx]:
            A[i] = left_array[left_idx]
            left_idx += 1
        else:
            A[i] = right_array[right_idx]
            right_idx += 1

def merge_sortion(A, low, high):
    if low == high:
        return
    else:
        mid = (low+high)/2
        merge_sortion(A, low, mid)
        merge_sortion(A, mid+1, high)
        merge(A, low, mid, high)

    return


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
    
    merge_sortion(A, 0, total_len-1)
    usage = time.time() -t
    print 'Sorted Array, usage=%f' %(usage)
    if print_list:
        print A
