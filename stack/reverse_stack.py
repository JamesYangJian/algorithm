from stack import *


class myStack(stack):
    def __init__(self):
        stack.__init__(self)

    def pop_bottom(self):
        if self.empty():
            raise Exception('Empty Stack')

        x = self.pop()
        if self.empty():
            return x
        else:
            y = self.pop_bottom()
            self.push(x)
            return y

    def reverse_stack(self):
        if self.empty():
            raise Exception('Empty stack')
        #self.dump()
        x = self.pop_bottom()
        if self.empty():
            self.push(x)
            return
        print 'pop bottom ' + str(x)
        self.reverse_stack()
        self.push(x)
        #self.dump()



if __name__ == '__main__':
    s = myStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    s.dump()
    #s.pop_bottom()
    s.dump()

    s.reverse_stack()
    s.dump()
