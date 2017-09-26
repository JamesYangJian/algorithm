
import sys

def LEFT(i):
    return ((i+1)<<1)-1

def RIGHT(i):
    return (((i+1)<<1)+1)-1

def PARENT(i):
    return ((i+1)>>1)-1

class heap:
    def __init__(self, A):
        self.A = A
        self.heap_size = len(A)

    def max_heapify_non_recursive(self, i):
        root = i
        left = LEFT(root)
        while left < self.heap_size:
            right = RIGHT(root)

            largest = root
            if self.A[left] > self.A[largest]:
                largest = left
            if right < self.heap_size and self.A[right] > self.A[largest]:
                largest = right

            if largest == root:
                break
            else:
                self.A[root], self.A[largest] = self.A[largest], self.A[root]
                root = largest
                left = LEFT(root)
            

    def max_heapify(self, i):

        left = LEFT(i)
        right = RIGHT(i)
        largest = i
        #print '  ----i=%d, val=%d, left=%d right=%d' %(i, A[i], left, right)
        if left < self.heap_size and self.A[left] > self.A[i]:
            largest = left
            #print '  ----left=%d, val=%d' %(left, A[left])

        if right < self.heap_size and self.A[right] > self.A[largest]:
            largest = right
            #print '  ----right=%d, val=%d' %(right, A[right])

        #print '  ----max=%d, val=%d' %(largest, A[largest])

        if largest != i:
            self.A[largest], self.A[i] = self.A[i], self.A[largest]
            self.max_heapify(largest)

    def build_max_heap(self):

        start = self.heap_size/2 - 1
        for i in xrange(start, -1, -1):
            #self.max_heapify(i)
            self.max_heapify_non_recursive(i)
            #print 'max_heapify, idx=%d' %(i)
            #print A

    def heap_sort(self):
        #B = []
        self.build_max_heap()

        for i in xrange(self.heap_size-1, 0, -1):
            self.A[0], self.A[i] = self.A[i], self.A[0]
            #B.insert(0, self.A[i])
            #A.pop(i)
            self.heap_size -= 1
            #max_heapify(A, 0)
            self.max_heapify_non_recursive(0)

        #B.insert(0, self.A[0])

        #return B


def heap_sort(A):
    h = heap(A)
    return h.heap_sort()


