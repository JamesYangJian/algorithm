"""
Quick-sort:
1. Choose a pivot value, partition the array, make left_array less than pivot
value and right_array bigger than pivot value
2. Quick left-array
3. Quick right-array
Whatever pivot is choosen, must change it to the beginning of the array
In this algorithm, i=low, j=high, partition is to start loop from j to find element
less than pivot, exchange elements in i and j, and then loop from
j to find the first pivot bigger than pivot, exchange elements in and j. Use
this alternative way to approach the final position of pivot value.
When end condition (i=j) met, let A[i] = pivot, return i
"""

import sys
import time
import copy
import time
import random


def Partition(A, low, high):
    i = low
    j = high
    pivot = A[i]

    while i < j:
        while A[j] >= pivot and i < j:
            j -= 1
        A[i], A[j] = A[j], A[i]
        while A[i] <= pivot and j > i:
            i += 1
        A[i], A[j] = A[j],A[i]

    A[i] = pivot

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

