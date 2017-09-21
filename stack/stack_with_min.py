
from stack import *


class stack_with_min:
    def __init__(self):
        self._stack_data = stack()
        self._stack_min = stack()

    def push(self, x):
        self._stack_data.push(x)

        if self._stack_min.empty():
            self._stack_min.push(x)
        else:
            min = self._stack_min.peek()
            if x < min:
                self._stack_min.push(x)
            else:
                self._stack_min.push(min)

    def pop(self):
        if self._stack_data.empty():
            raise Exception('Stack is empty')
        else:
            self._stack_min.pop()
            return self._stack_data.pop()

    def get_min(self):
        if self._stack_min.empty():
            return None
        else:
            return self._stack_min.peek()
