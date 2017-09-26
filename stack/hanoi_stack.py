
import sys

from stack import *

L_M = 1
M_L = 2
M_R = 3
R_M = 4

def move(action, stack_left, stack_mid, stack_right):
    if action == L_M:
        x = stack_left.pop()
        print 'Move %d from left to mid' % (x)
        stack_mid.push(x)
    elif action == M_L:
        x = stack_mid.pop()
        print 'Move %d from mid to left' % (x)
        stack_left.push(x)
    elif action == M_R:
        x = stack_mid.pop()
        print 'Move %d from mid to right' % (x)
        stack_right.push(x)
    elif action == R_M:
        x = stack_right.pop()
        print 'Move %d from right to mid' % (x)
        stack_mid.push(x)


def hanoi_stack(N, stack_left, stack_mid, stack_right):
    if N <= 0 or stack_left.depth() != N:
        return

    if stack_mid.depth() > 0 or stack_right.depth() > 0:
        return

    prohibited = 0

    while stack_right.depth() < N:
        action = 0
        if prohibited != L_M and not stack_left.empty():
            if stack_mid.empty() or stack_left.peek() < stack_mid.peek():
                action = L_M
                prohibited = M_L

        if action == 0 and prohibited != M_L and not stack_mid.empty(): 
            if stack_left.empty() or stack_left.peek() > stack_mid.peek():
                action = M_L
                prohibited = L_M

        if action == 0 and prohibited != M_R and not stack_mid.empty():
            if stack_right.empty() or stack_mid.peek() < stack_right.peek():
                action = M_R
                prohibited = R_M
        
        if action == 0:
            action = R_M
            prohibited = M_R

        move(action, stack_left, stack_mid, stack_right)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python ./hanoi_stack.py number'
        sys.exit(0)

    N = int(sys.argv[1])

    stack_left = stack()
    stack_right = stack()
    stack_mid = stack()

    for i in xrange(N, 0, -1):
        stack_left.push(i)

    stack_left.dump()
    hanoi_stack(N, stack_left, stack_mid, stack_right)
    stack_right.dump()
            






