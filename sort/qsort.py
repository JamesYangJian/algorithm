import sys
import time
import copy
import time
import random

def Random_Partition(A, low, high):
    i = random.randint(low, high)
    pivot = A[i]

    A[low], A[i] = A[i], A[low]
    i = low
    j = low+1

    while j <= high:
        if A[j] > pivot:
            j += 1
        else:
            A[i+1], A[j] = A[j], A[i+1]
            i += 1
            j += 1

    A[low], A[i] = A[i], A[low]
    return i


def Partition(A, low, high):
    i = low
    pivot = A[i]
    j = low+1

    while j <= high:
        if A[j] > pivot:
            j += 1
        else:
            A[i+1], A[j] = A[j], A[i+1]
            i += 1
            j += 1

    A[low], A[i] = A[i], A[low]
    return i

def QSort(A, low, high):
    if low>=high:
        return
    else:
        mid = Partition(A, low, high)
        QSort(A, low, mid-1)
        QSort(A, mid+1, high)


if __name__ == '__main__':
    random.seed(time.time())
    print_list = False
    total_len = int(sys.argv[1])
    if (len(sys.argv) > 2) and sys.argv[2] == 'p':
        print_list = True

    A = []
    for i in xrange(0,total_len):
        A.append(random.randint(-1000000, 1000000))

    print 'Original Array'
    if print_list:
        print A
    t = time.time()
    
    QSort(A, 0, total_len-1)
    usage = time.time() -t
    print 'Sorted Array, usage=%f' %(usage)
    if print_list:
        print A
