import random
import sys
from stack import *

def push_stack_by_order(x, s_dest, s_aux):
    if s_dest.empty():
        s_dest.push(x)
        return

    cur = s_dest.peek()
    if x <= cur:
        s_dest.push(x)
    else:
        s_aux.push(s_dest.pop())
        push_stack_by_order(x, s_dest, s_aux)

def stack_order(s_a, s_h):

    #if s_a.empty():
    #   while not s_h.empty():
    #        s_a.push(s_h.pop())

    while not s_a.empty():
        x = s_a.pop()
        push_stack_by_order(x, s_h, s_a)
        #stack_order(s_a, s_h)

    while not s_h.empty():
        s_a.push(s_h.pop())


if __name__ == '__main__':
    sys.setrecursionlimit(10240)
    num = int(sys.argv[1])
    s_a = stack()
    s_h = stack()

    for i in xrange(0, num):
        x = random.randint(0, 10000)
        s_a.push(x)

    s_a.dump()

    stack_order(s_a, s_h)

    s_a.dump()


