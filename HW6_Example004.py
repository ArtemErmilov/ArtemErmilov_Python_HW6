# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


from functools import reduce
import numbers
from os import system
system ('cls')
import Base

list_data= ["qwe", "asd", "zxc", "qwe", "ertqwe"]
data ="qwe"

list_index = [i for i,x in enumerate(list_data) if data ==x] 


try:
    if list_index[1]!=None:
        number=list_index[1]
except IndexError:
    number = -1
    
print(f'список:{list_data} ищем: {data} ответ {number}')