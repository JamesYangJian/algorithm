
def partition(L, start, end):

    if start == end:
        return start

    pivot = start
    idx = start + 1
    cur = start + 1

    if L[pivot] > L[idx]:
        L[pivot], L[idx] = L[idx], L[pivot]

    val_pivot = L[start]

    while cur <= end:
        if val_pivot > L[cur]:
            L[idx], L[cur] = L[cur], L[idx]
            idx += 1
        cur += 1

    L[pivot], L[idx-1] = L[idx-1], L[pivot]

    return idx-1

def QSort(L, start, end):
    idx = partition(L, start, end)

    if idx > start:
        QSort(L, start, idx-1)

    if idx < end:
        QSort(L, idx+1, end)

def find_least_m_num(L, m):
    if m > len(L):
        raise Exception('m is out of range!')

    left = 0
    end = len(L) - 1
    idx = -1
    round = 0

    while idx != m -1:
        round += 1

        idx = partition(L, left, end)
        if idx > m - 1:
            left = left
            end = idx - 1
        else:
            left = idx +1
            end = end

    return round




if __name__ == '__main__':
    import sys
    import random

    if len(sys.argv) < 2:
        num = 10
    else:
        num = int(sys.argv[1])


    L = [random.randint(0, 1000) for i in range(num)]

    print(L)

    #QSort(L, 0, len(L)-1)
    m = num // 3
    print("Find %d least element in L" % m)
    rnd = find_least_m_num(L, m)

    print(L)
    print("Usage: %d" % rnd)
          
