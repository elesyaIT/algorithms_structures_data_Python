# 1.удаление элементов списка
# list_4 = [1,2,3,4]
#
# for i, item in enumerate(list_4[:]):
#     list_4.remove(item)
# print(list_4)

# 2.Крестики нолики
# broad = [[''] * 3 for i in range(3)]
# broad[0][0]='x'
# print(broad)

# 3.Те же операнды, но другая история
# a = [1,2,3,4]
# b = a
# a = a + [5,6,7]
# print(a,b)
#
# a = [1,2,3,4]
# b = a
# a += [5,6,7]
# print(a,b)

# 4. Игла в стоге сена
# t = ('one','two')
# for i in t:
#     print(i)
#
# d = ('one',)
# for i in d:
#     print(i)

# Ключ словаря - изменяемый объект
set_x = {1,2,3}
list_y = [5,6,7]
dict_x = {frozenset(set_x):list_y}
print(dict_x)
dict_y = {tuple(list_y):set_x}
print(list_y)
