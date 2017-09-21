

class stack:
    def __init__(self):
        self._list = []

    def push(self, x):
        self._list.insert(0, x)

    def empty(self):
        if len(self._list):
            return False
        else:
            return True

    def pop(self):
        if self.empty():
            return None
        else:
            return self._list.pop(0)

    def peek(self):
        if self.empty():
            return None
        else:
            return self._list[0]

    def dump(self):
        print self._list
