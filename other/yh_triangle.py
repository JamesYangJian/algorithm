#!/usb/bin/python


def yh_triangle():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0]+a, a+[0])]


def yh_triangle2():
    a = [1]
    while True:
        yield a
        a = list(map(lambda x, y:x+y, [0]+a, a+[0]))

if __name__=='__main__':
    count = 0
    ts = yh_triangle()
    for t in ts:
        print t
        count += 1
        if count == 10:
            break
