def naive_max_perm_rec(M, A=None):
    if A is None:
        A = set(range(len(M)))

    if len(A) == 1:
        return A
    B = set(M[i] for i in A)

    C = A - B
    if C:
        A.remove(C.pop())
        return naive_max_perm_rec(M, A)

    return A

def naive_max_perm(M):
    A = set(range(len(M)))
    B = set(M[i] for i in A)
    C = A - B

    while len(C) > 0:
        A.remove(C.pop())
        B = set(M[i] for i in A)
        C = A-B

    return A

def max_perm_2(M):
    left = set()
    for i in range(len(M)):
        if M[i] == M[M[i]]:
            left.update([i])
        elif i == M[M[i]]:
            left.update([i, M[i]])

    return left



if __name__ == '__main__':
    M = [2, 2, 0, 1, 3, 5, 7, 4]

    print(M)

    A = naive_max_perm_rec(M)

    print(A)

    C = naive_max_perm(M)
    print(C)

    B = max_perm_2(M)

    print(B)
