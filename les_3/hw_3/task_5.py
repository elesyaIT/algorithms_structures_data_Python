"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию
 в массиве.
"""
from random import randint
a = [randint(-15,15) for i in range(15)]
b = sorted(a)
for i in b:
    if i>=0:
        break
    c=i
if c<0:
    n_ind=a.index(c)
    print(f'Число {c}, по индексу {n_ind}')
else:
    print("Нет отрицательных значений")
