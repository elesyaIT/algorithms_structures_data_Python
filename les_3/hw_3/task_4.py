"""
4. Определить, какое число в массиве встречается чаще всего.
"""
from random import randint
a = [randint(0,8) for i in range(15)]
b = list(set(a))
print(a)
print(b)
c=1
for i in b:
    s = a.count(i)
    if s>c:
        c=s
        f = f'Число {i} встречается {c}'
if s==c:
    print("одинаковое количество")
else:
    print(f)

