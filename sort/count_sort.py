
def count_sort(A, max):
    length = len(A)
    if length <= 0:
        raise Exception('Zero length array!')

    B = []
    C = []

    for i in xrange(0, length):
        B.append(0)

    for i in xrange(0, max+1):
        C.append(0)

    for i in xrange(0, length):
        C[A[i]] += 1

    for i in xrange(1, max+1):
        C[i] = C[i] + C[i-1]

    for i in xrange(length-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return B


