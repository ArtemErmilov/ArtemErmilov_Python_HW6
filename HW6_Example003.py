#3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)




from functools import reduce
from os import system
system ('cls')
import Base

number_str = input('Введите координаты 2-х точек через пробел: ')

list_coordinat = number_str.split()
list_coordinat = list(map(int,[x for x in list_coordinat]))

A=list(map(lambda x: x,[list_coordinat[:2:]]))
B = list(map(lambda x: x,[list_coordinat[2::]]))

y =(reduce(lambda x1,x2: (x2-x1)**2, list_coordinat[::2])+reduce(lambda y1,y2: (y2-y1)**2, list_coordinat[1::2]))**0.5

print(f'Расстояние между точками A{A} и B{B} = {y}')