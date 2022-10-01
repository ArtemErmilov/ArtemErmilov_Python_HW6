# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3



from ast import Break, Lambda
from os import system
system ('cls')
import Base


list_number=['gfh5', 'gfh2', '67', 'jy32', '3put']

print (list_number)

number = str(int(Base.check_number('Введите число: ')))



list_index=[i for i,x in enumerate(list_number) if x.find(number)>-1]

try:
    if list_index[0]!=None:
        print(f'{list_number} ищем {number} находим на позиции: {list_index}')
except IndexError:
    print(f'{list_number} число {number} не в списке присутствует')

    
