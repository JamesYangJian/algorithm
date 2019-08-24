# -*- coding: utf-8 -*-

from heapq import heapify, heappop, heappush
from itertools import count

"""
huffman encoding:
https://blog.csdn.net/qq_29519041/article/details/81428934

1. 统计词频， 类似 {"a": 4, "b": 5, "c": 6, "d": 9, "e": 11, "f": 11, "g": 15, “h": 1 , "i": 20}
2. 去掉频率最小的两个， 合并， 小的在左边，大的在右边，频率相加，然后merge回列表中
3. 重复2， 直到列表中只有两个元素

最后形如：
[[['c', 'd'], 'i'], [[['b', ['h', 'a']], 'e'], ['f', 'g']]]
('c', '000')
('d', '001')
('i', '01')
('b', '1000')
('h', '10010')
('a', '10011')
('e', '101')
('f', '110')
('g', '111')

可以看到，词频越高的搜索路径越短，词频越低的搜索路径越长，且在同一层的节点按频率从低到高排列

"""

def huffman(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq))
    heapify(trees)
    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa+fb, n, [a, b]))

    return trees[0][-1]

def codes(tree, prefix=''):
    if len(tree) == 1:
        yield(tree, prefix)
        return

    for bit, child, in zip('01', tree):
        for pair in codes(child, prefix + bit):
            yield pair

if __name__ == '__main__':
    seq = 'abcdefghi'
    frq = [4, 5, 6, 9, 11, 11, 15, 1, 20]

    ret = huffman(seq, frq)

    print(ret)

    code_list = codes(ret, 'James')
    try:
        for i in code_list:
            print(i)
    except:
        pass