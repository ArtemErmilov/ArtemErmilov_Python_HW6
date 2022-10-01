# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.



from functools import reduce
import numbers
from os import system
system ('cls')
import Base



amount = Base.check_number('Введите число: ')

list_number=[(-3)**x for x in range(int(amount))]

print(list_number)