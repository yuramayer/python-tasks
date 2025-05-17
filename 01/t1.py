# flake8: noqa
# pylint: disable=all
# pylint: enable=undefined-variable, no-member, used-before-assignment, import-error

string = 'ajklfewqj12jlkzf48asjljAFcxz,,rqf .fda07'

# берём множество
# стоимость множества = O(n),
#   просто прошлись разок и сделали хэш,
#       и каждый символ добавляем за O(1)
all_symbols = set(string) 
print(len(all_symbols), len(string))
# длина этого множества - длина искомой подстроки.

# например, длина all_symbols получилась 25, а длина string = 40.
# получается что мы можем каждый раз проходить 

