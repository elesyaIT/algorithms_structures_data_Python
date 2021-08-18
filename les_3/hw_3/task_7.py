"""
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба минимальны), так и различаться.
"""
from random import randint

a = [randint(0, 15) for i in range(15)]
print(a)
# m_1 = a.pop(a.index(min(a)))
# m_2 = a.pop(a.index(min(a)))
m_1 = min(a)
a.remove(m_1)
m_2 = min(a)
print(m_1, m_2)