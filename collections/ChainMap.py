from collections import ChainMap

d_1 = {'a':2,'b':5,'c':7}
d_2 = {'a':10,'b':20,'d':45}

d_map = ChainMap(d_1, d_2)
print(d_map)

d_2['a']=100
print(d_map)

print(d_map['a'])
print(d_map['d'])




# методы ChainMap

# добавляем словарь в начало
x = d_map.new_child()
print(x)

# обращение по индексу к словарю
print(x.maps[0])
print(x.maps[1])

#
print(x.parents)
