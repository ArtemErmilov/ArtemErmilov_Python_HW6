
#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

from functools import reduce
import numbers
from os import system
from random import randint
system ('cls')
import Base


list_number = [randint(1,5) for x in range(10)]

list_mul = [x*list_number[-(i+1)] for i,x in enumerate (list_number[:len(list_number)//2+len(list_number)%2])]


print (list_number)
print (list_mul)