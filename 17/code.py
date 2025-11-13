"""17th code"""


lst = [1, 2, 5, 2, 7, 10, 12]

# чтобы решить оптимально,
# сначала найдём произведение,
# а потом будем делить

# отдельная история с нулями

def func(lst):
    if not lst:
        return 0
    prod = 1
    zero_counter = 0
    for elem in lst:
        if elem == 0:
            zero_counter += 1
            continue
        prod *= elem
    
    res = []

    if zero_counter == 0:
        for elem in lst:
            res.append(prod // elem)
    elif zero_counter == 1:
        for elem in lst:
            if elem == 0:
                res.append(prod)
            else:
                res.append(0)
    else:
        for elem in lst:
            res.append(0)
    return res
