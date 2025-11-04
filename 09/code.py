def merge(self, nums1, m, nums2, n):
    """
    Если идём с начала, то затираем значения

    Поэтому мы пойдём с конца!
    """ 
    # nums1_ix = индекс последнего настоящего элемента в nums1
    nums1_ix = m - 1
    
    # nums2_ix = индекс последнего элемента в nums2
    nums2_ix = n - 1

    # k = индекс последней позиции в nums1
    k = m + n - 1

    # пока оба массива не закончились
    while nums1_ix >= 0 and nums2_ix >= 0:

        # сравниваем последние элементы
        if nums1[nums1_ix] > nums2[nums2_ix]:

            # большой ставим в конец nums1
            nums1[k] = nums1[nums1_ix]
            
            # сдвигаем указатель влево в nums1
            nums1_ix -= 1
        
        else:
            nums1[k] = nums2[nums2_ix]

            # сдвигаем указатель слево в nums2
            nums2_ix -= 1

        k -= 1 # всегда проходим влево массива
    
    # добавляем если в nums2 что-то осталось
    while nums2_ix >= 0:
        nums1[k] = nums2[nums2_ix]
        nums2_ix -= 1
        k -= 1