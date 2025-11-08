"""13th task"""


data = [(1,3), (2,6), (8,10), (15,18)]


"""
Сначала отсотрируем по началу. n log(n)

Затем на каждом следующем этапе будем проверять,
попали ли мы к прошлому

Если попали - создаём новый temp-интервал

Если нет - сохраняем прошлый и создаём новый
"""

def func(data):

    data = sorted(data, key=lambda x: x[0])

    res = []
    tmp = None

    for tpl in data:
        start, end = tpl

        if tmp is None:
            tmp = (start, end)
            continue

        prev_start, prev_end = tmp
        if start <= prev_end:
            tmp = (prev_start, max(prev_end, end))
            continue
        else:
            res.append(tmp)
            tmp = (start, end)


    if tmp is not None:
        res.append(tmp)
    return res