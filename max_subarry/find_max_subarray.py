"""
Find the max sub-array question
Use divide-conquer-combine strategy
1, Divide an array into two equal part
2, Find max sub-array in the left side,Find max sub-array in the right side, Find max
sub-array crossing the middle position
3. Compare the max value of the three part, return the maximum one

T(n) = 2(T/2n) + Theta(n) = Theta(nlgn)
"""


import sys
import time
import random


def find_max_cross_array(A, low, mid, high):
    left_max = -sys.maxint-1
    left_idx = mid
    left_sum  = 0

    for i in xrange(mid, low-1, -1):
        left_sum = left_sum + A[i]
        if left_sum > left_max:
            left_max = left_sum
            left_idx = i

    right_max = -sys.maxint - 1
    right_idx = mid
    right_sum = 0
    
    for i in xrange(mid+1, high+1, 1):
        right_sum += A[i]
        if right_sum > right_max:
            right_max = right_sum
            right_idx = i

    return (left_idx, right_idx, left_max+right_max)


def find_max_subarray(A, low, high):
    left_low = -1
    left_high = -1
    right_low = -1
    right_high = -1
    cross_left = -1
    cross_right = -1
    left_max = 0
    right_max = 0
    cross_max = 0


    if low == high:
        left_low = left_high = low
        left_max = A[low]
        return (left_low, left_high, left_max)
    else:
        mid = (high+low)/2
        # print 'Calc left, low=%d, high=%d' %(low, mid)
        left_low, left_high, left_max = find_max_subarray(A, low, mid)
        # print 'Calc right, low=%d, high=%d' %(mid+1, high)
        right_low, right_high, right_max = find_max_subarray(A, mid+1, high)
        cross_left, cross_right, cross_max = find_max_cross_array(A, low, mid,
                high)

        if left_max >= right_max and left_max >= cross_max:
            return (left_low, left_high, left_max)
        elif right_max >= left_max and right_max >= cross_max:
            return (right_low, right_high, right_max)
        else:
            return (cross_left, cross_right, cross_max)

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





        


