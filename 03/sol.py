def cons_int(A):

    if not A:
        return 0
    
    a_set = set(A)
    best = 0

    for elem in a_set:
        if (elem - 1) not in a_set:

            length = 1
            next_val = elem + 1

            while next_val in a_set:
                length += 1
                next_val += 1
            
            if length > best:
                best = length
    
    return best

print(cons_int([10, 4, 20, 1, 3, 2])) 