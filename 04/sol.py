def missin(A):

    a_set = set(A)
    smallest = 0
    
    is_searching = True

    while is_searching:
        if smallest + 1 in a_set:
            smallest += 1
        else:
            is_searching = False
    smallest += 1

    return smallest

print(missin([1, 2, 5, 3, -2, 5, 7, 9]))
