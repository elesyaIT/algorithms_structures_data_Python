"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
элементами. Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

a = [randint(0, 15) for i in range(15)]
print(a)
mn = a.index(min(a))
mx = a.index(max(a))
if mx>mn:
    ls = a[mn+1:mx]
elif mx<mn:
    ls = a[mn -1:mx:-1]
print(sum(ls))