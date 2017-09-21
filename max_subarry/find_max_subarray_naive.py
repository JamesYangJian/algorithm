import sys
import time
import random

def find_max_subarray(A, low, high):
    max = -sys.maxint -1
    left_idx = low
    right_idx = low
    sum = 0

    for i in xrange(low, high+1):
        sum = A[i]
        if sum > max:
            max = sum
            left_idx = i
            right_idx = i
        for j in xrange(i+1, high+1):
            sum += A[j]
            if sum > max:
                max = sum
                left_idx = i
                right_idx = j

    return (left_idx, right_idx, max)



if __name__ == '__main__':
    A = []
    print_list = False

    length = int(sys.argv[1])
    if len(sys.argv) > 2 and sys.argv[2] == 'p':
        print_list = True

    random.seed(time.time())
    for i in xrange(0, length, 1):
        A.append(random.randint(-20, 20))

    if print_list:
        print A

    t = time.time()

    left, right, max = find_max_subarray(A, 0, length-1)
    usage = time.time() - t 

    print 'left=%d, right=%d, max=%d, usage=%f' %(left, right, max, usage)




