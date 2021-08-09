"""
3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
"""
import random

print('Ведите границы для случайного целого числа:')
i_1 = int(input('нижняя граница = '))
i_2 = int(input('верхняя граница = '))
print('Ведите границы для случайного вещественного числа:')
f_1 = float(input('нижняя граница = '))
f_2 = float(input('нижняя граница = '))
print('Ведите границы для случайной буквы:')
letter1 = input('letter 1 = ')
letter2 = input('letter 2 = ')

ram_int = random.randint(i_1, i_2)
ram_float = random.uniform(f_1, f_2)
ram_char = chr(random.randint(ord(letter1), ord(letter2)))

print(f'Случайное целое число: {ram_int}\n'
      f'Случайное вещественное число: {ram_float}\n'
      f'Случайная буква: {ram_char}')