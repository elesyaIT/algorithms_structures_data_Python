from collections import defaultdict
# a = defaultdict()
# print(a)
#
# s = 'uytiuyiuwetuirhgjskhiewrgewjsvn'
# b = defaultdict(int)
# for i in s:
#     b[i] += 1
# print(b)

# list_1 = [('cat',1),('dog',2),('cat',5),('mouse',4),('cat',7)]
# c = defaultdict(list)
# for k,v in list_1:
#     c[k].append(v)
# print(c)

# list_2 = [('cat',1),('dog',2),('cat',5),('mouse',4),('cat',7),('dog',2)]
# c = defaultdict(set)
# for k,v in list_2:
#     c[k].add(v)
# print(c)

f = defaultdict(lambda: 'unknown')
f.update(rex='dog',tomas='cat')
print(f)
print(f['rex'])
print(f['jerry'])
