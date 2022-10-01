#2- Найти сумму чисел списка стоящих на нечетной позиции



from ast import Break, Lambda
from functools import reduce
from os import system
from random import randint
system ('cls')
import Base

list_number=[randint(1,5) for x in range(10)]

sum_number= (reduce(lambda el1, el2: el1+el2,[x for x in list_number[1::2]]))

print(list_number)
print (f'Сумма на нечётных позициях = {sum_number} ')