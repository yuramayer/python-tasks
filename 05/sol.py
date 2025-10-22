def top_freq(nums, k):

    freq = {}

    for el in nums:
        freq[el] = freq.get(el, 0) + 1
    
    opfreq = {}

    for key, value in freq.items():
        if value in opfreq:
            opfreq[value] = opfreq[value] + [key]
        else:
            opfreq[value] = [key]
    
    search_freq = len(nums)
    res = []

    while k > 0:
        if search_freq < 1:
            break
        if search_freq in opfreq:
            res.extend(opfreq[search_freq])
            k -= 1
        search_freq -= 1

    return res


print(top_freq([1, 1, 1, 1, 1, 3, 2, 2, 1, 5, 2, 2, 4, 1, 1, 2, 4], 3))
