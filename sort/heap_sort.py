
import sys

def LEFT(i):
    return ((i+1)<<1)-1

def RIGHT(i):
    return (((i+1)<<1)+1)-1

def PARENT(i):
    return ((i+1)>>1)-1

def max_heapify_non_recursive(A, i):
    heap_size = len(A)

    root = i
    left = LEFT(root)
    while left < heap_size:
        right = RIGHT(root)

        largest = root
        if A[left] > A[largest]:
            largest = left
        if right < heap_size and A[right] > A[largest]:
            largest = right

        if largest == root:
            break
        else:
            A[root], A[largest] = A[largest], A[root]
            root = largest
            left = LEFT(root)
        

def max_heapify(A, i):
    heap_size = len(A)

    left = LEFT(i)
    right = RIGHT(i)
    largest = i
    #print '  ----i=%d, val=%d, left=%d right=%d' %(i, A[i], left, right)
    if left < heap_size and A[left] > A[i]:
        largest = left
        #print '  ----left=%d, val=%d' %(left, A[left])

    if right < heap_size and A[right] > A[largest]:
        largest = right
        #print '  ----right=%d, val=%d' %(right, A[right])

    #print '  ----max=%d, val=%d' %(largest, A[largest])

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest)

def build_max_heap(A):
    size = len(A)

    start = size/2 - 1
    for i in xrange(start, -1, -1):
        #max_heapify(A, i)
        max_heapify_non_recursive(A, i)
        #print 'max_heapify, idx=%d' %(i)
        #print A

def heap_sort(A):
    heap_size = len(A)
    B = []
    build_max_heap(A)

    for i in xrange(heap_size-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        B.insert(0, A[i])
        A.pop(i)
        #max_heapify(A, 0)
        max_heapify_non_recursive(A, 0)

    B.insert(0, A[0])

    return B





