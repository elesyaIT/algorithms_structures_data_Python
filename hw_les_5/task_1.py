"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
 для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
  и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple
from statistics import mean

New_Company = namedtuple('New_Company', 'name profit_list avg')

lst = []
for i in range(int(input('Введите количество компани '))):
    arg = input('Введите в строку имя и поквартальную прибыль через пробел:\n').split()
    lst.append(New_Company(arg[0], arg[1:], mean(map(int, arg[1:3]))))

avg = mean([i.avg for i in lst])

for i in lst:
    print(f'Компания: {i.name} \t\tСредняя прибыль за год: {i.avg}')

print('_' * 70, '\n')

print('Компании с прибылью меньше средней:')
for i in lst:
    if i.avg < avg:
        print(i.name)

print('Компании с прибылью больше средней:')
for i in lst:
    if i.avg > avg:
        print(i.name)


# 2 вариант
# from collections import defaultdict
#
# companies = defaultdict()
# company_cnt = int(input("Введите количество предприятий: "))
#
# while company_cnt:
#     print("*" * 30)
#     name = input("Введите название предприятия: ")
#     companies[name] = float(input("Введите годовую прибыль предприятия: "))
#     company_cnt -= 1
#
#
# average = sum(companies.values()) / len(companies)
#
# print(f"Среднегодовая прибыль {len(companies)} предприятий составляет {average} руб")
#
# for name, profit in companies.items():
#     if profit > average:
#         print(f"Предприятие {name} имеет доход выше среднегодового")
#     elif profit < average:
#         print(f"Предприятие {name} имеет доход ниже среднегодового")
