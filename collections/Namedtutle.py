from collections import namedtuple

# hero_1 = ('Aaz','Izverg',100,0,250)
#
# class Person:
#
#     def __init__(self,name, race, healtg, mana, strength):
#         self.name = name
#         self.race = race
#         self.healtg = healtg
#         self.mana = mana
#         self.strength = strength
#
# hero_2 = Person('Aaz','Izverg',100,0,250)
# print(hero_2.mana)

# New_Person = namedtuple('New_Person','name, race, healtg, mana, strength')
# hero_3 = New_Person('Aaz','Izverg',100,0,250)
# print(hero_3.strength)
#
# prop = ['name','race','healtg','strength']
# New_Person_1 = namedtuple('New_Person',prop, rename=True) # rename=True -- если не коррек имена _healtg
# hero_4 = New_Person('Aaz','Izverg',100,0,250)
# print(hero_4.name)

# Point = namedtuple('Point','x,y,z')
#
# p1 = Point(1,z=3,y=4)
# print(p1)
#
# t = [5,7,10]
# p2 = Point._make(t)
# print(p2)
#
# d2 = p2._asdict()
# print(d2)
#
# # кортедж не изм, чтобы поменять созд. новый объукт
# p3=p2._replace(x=6)
# print(p3)
#
# # посмотреть поля кортеджа
# print(p3._fields)

# значения по умолчанию
New_Point = namedtuple("New_Point",'x,y,z', defaults=[0,0])
# p4 =New_Point(7)
# print(p4)
#
# print(p4._field_defaults)

dct = {'x':30,'y':25,'z':55}
p5 = New_Point(**dct)
print(p5)


