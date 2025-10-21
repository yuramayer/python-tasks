def lists2list(A, B):
    i = 0
    j = 0
    C = []
    while i < len(A) and j < len(B):
        a_elem = A[i]
        b_elem = B[j]
        if a_elem > b_elem:
            C.append(b_elem)
            j += 1
        else:
            C.append(a_elem)
            i += 1
    if i < len(A):
        C.extend(A[i:])
    if j < len(B):
        C.extend(B[j:])
    return C

A = [1, 2, 3, 3, 5, 9]
B = [0, 2, 4, 6, 8, 11, 12, 19]

lists2list(A, B)
