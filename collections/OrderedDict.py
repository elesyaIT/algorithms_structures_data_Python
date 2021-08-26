from collections import OrderedDict

from django.template.defaultfilters import last

a= {'cat':5,'mouse':7, 'dog':4,}
new_a = OrderedDict(sorted(a.items(), key=lambda x:x[0]))
print(new_a)

b= {'cat':5,'mouse':7, 'dog':4,}
new_b = OrderedDict(sorted(a.items(), key=lambda x:x[1]))
print(new_b)

print(new_a==new_b)

# перенесет в конец словаря
new_b.move_to_end('mouse')
print(new_b)
# перенесет в начало словаря
new_b.move_to_end('mouse', last=False)
print(new_b)
