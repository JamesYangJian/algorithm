import sys

class pillar:
    def __init__(self, name):
        self.name = name


def move(n, src_pillar, dst_pillar):
    print 'Move plate %d from %s to %s' %(n, src_pillar.name, dst_pillar.name)


def hanoi(N, src_pillar, aux_pillar, dst_pillar):
    if N == 1:
        move(N, src_pillar, dst_pillar)
        return

    hanoi(N-1, src_pillar, dst_pillar, aux_pillar)
    move(N, src_pillar, dst_pillar)
    hanoi(N-1, aux_pillar, src_pillar, dst_pillar)

    return

def hanoi_new(N, src_pillar, aux_pillar, dst_pillar):
    if N == 1:
        move(N, src_pillar, aux_pillar)
        move(N, aux_pillar, dst_pillar)
        return

    hanoi_new(N-1, src_pillar, aux_pillar, dst_pillar)
    move(N, src_pillar, aux_pillar)
    hanoi_new(N-1, dst_pillar, aux_pillar, src_pillar)
    move(N, aux_pillar, dst_pillar)
    hanoi_new(N-1, src_pillar, aux_pillar, dst_pillar)

    return

if __name__ == '__main__':
    new = False

    if len(sys.argv) < 2:
        print 'Usage: hanoi.py Number'
        sys.exit(0)

    if len(sys.argv) > 2 and sys.argv[2] == 'n':
        new = True

    N = int(sys.argv[1])
    left_pillar = pillar('left')
    right_pillar = pillar('right')
    mid_pillar = pillar('mid')
    if not new:
        hanoi(N, left_pillar, mid_pillar, right_pillar)
    else:
        hanoi_new(N, left_pillar, mid_pillar, right_pillar)

