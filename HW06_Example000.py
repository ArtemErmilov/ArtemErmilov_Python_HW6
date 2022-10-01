# Задание с семинара
# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;

# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
# (256 - 194 => некорректная запись скобок

import numbers
from operator import index, mul
from os import system
system ('cls')





def math_str(math:str):

    def breaking_math(math:str):

        list_number_attributes=[]
    
        
        number =''
        atribut = ''
        

        for y in  math:
            
            if  y=='*' and atribut!=y:
                atribut=y
            elif  atribut==y:
                list_number_attributes.append('**')
                atribut=''
            elif  atribut=='*' and atribut!=y:
                list_number_attributes.append('*')
                atribut=''
            if y.isdigit() == True:
                number+=y
            elif y.isdigit() == False:
                if number != '':
                    list_number_attributes.append(number)
                number =''
            if y.isdigit() == False and y!='*':
                if y!='':
                    list_number_attributes.append(y)
        if number != '':
            list_number_attributes.append(number)
        return list_number_attributes

    list_data=breaking_math(math)
    
    error =False

    for x in list_data:# Поверка на буквы 
        if x.isdigit()==False and x!='**'and x!='*'and x!='+'and x!='-'and x!='('and x!=')'and x!='/':
            error=True
    
    if list_data.count('(')!=list_data.count(')'):#Проверка парности скобок  
        error=True
    
    while list_data.count (')')>0 and list_data.count ('(')>0 and error ==False:# Проверка правильности установки скобок

        if list_data.index(')')>list_data.index('('):
            list_data.pop(list_data.index(')'))
            list_data.pop(list_data.index('('))
        elif list_data.index(')')<list_data.index('('):
            error=True

    list_data=breaking_math(math)
    index_1=0
    index_2=0
    for i, x in  enumerate(list_data):
        if x == '(':
            index_1=i 
        elif x == ')':
            index_2=i 
        if index_1+1==index_2:
            error=True
            break            
    
    index_1=-2
    index_2=-2
    index_3=-2
    index_max=0
    for i, x in  enumerate(list_data):
        index_max=i
        if x==')':
            index_3=i
        if x.isdigit()==False and x!='('and  x!=')':
            index_1=i
            if index_1-1==index_2 or index_3==index_2+1:
                error=True
                break
            else:         
                index_2=index_1
    if list_data[0]=='**' or list_data[0]=='*' or list_data[0]=='/':
        error=True

    if list_data[index_max].isdigit()==False and list_data[index_max]!=')':
        error=True


    if error==True:
        print('Пример введён не корректно ')
        return 


    def maths_list (list_number_attributes:list):

        if list_number_attributes[0]=='-':
            numbir_att = int(list_number_attributes[1])*(-1)
            for i in range(2): 
                list_number_attributes.pop(0)
            list_number_attributes.insert(0, str(numbir_att))

        elif  list_number_attributes[0]=='+':
            list_number_attributes.pop(0)


        while True:
            if list_number_attributes.count('**')>0:
                attr='**'
            elif list_number_attributes.count('*')>0 or list_number_attributes.count('/')>0:
                if list_number_attributes.count('*')>0 and list_number_attributes.count('/')>0 :
                    if list_number_attributes.index('*')<list_number_attributes.index('/'):
                        attr='*'
                    elif list_number_attributes.index('/')<list_number_attributes.index('+'):
                        attr='/'
                elif list_number_attributes.count('*')>0:
                    attr='*'
                else:
                    attr='/'
            elif list_number_attributes.count('+')>0 or list_number_attributes.count('-')>0:
                if list_number_attributes.count('+')>0 and list_number_attributes.count('-')>0 and (list_number_attributes.index('+')<list_number_attributes.index('-')):
                    attr='+'
                elif list_number_attributes.count('-')>0 and list_number_attributes.count('+')>0 and (list_number_attributes.index('-')<list_number_attributes.index('+')):
                    attr='-'
                elif list_number_attributes.count('+')>0:
                    attr='+'
                else:
                    attr='-'
            else:
                break
            
            index_attribute = list_number_attributes.index(attr)
            if attr=='**':
                temp_number=float(list_number_attributes[index_attribute-1])**float(list_number_attributes[index_attribute+1])
            elif attr=='*':
                temp_number=float(list_number_attributes[index_attribute-1])*float(list_number_attributes[index_attribute+1])
            elif attr=='/':
                temp_number=float(list_number_attributes[index_attribute-1])/float(list_number_attributes[index_attribute+1])
            elif attr=='+':
                temp_number=float(list_number_attributes[index_attribute-1])+float(list_number_attributes[index_attribute+1])
            elif attr=='-':
                temp_number=float(list_number_attributes[index_attribute-1])-float(list_number_attributes[index_attribute+1])
            temp_number=str(temp_number)    
            for i in range(3):
                list_number_attributes.pop(index_attribute-1)

            list_number_attributes.insert(index_attribute-1,temp_number)
        
        number_maths = list_number_attributes[0]
        return number_maths

    


    def quotes_math(math_in:str):

        
        list_number_attributes=breaking_math(math_in)
        while list_number_attributes.count('(')>0:
            index_el_1=0
            index_el_2=0

            for i,x in enumerate (list_number_attributes):
                if x=='(':
                    index_el_1=i
                if x==')':
                    index_el_2=i
                    break

            new_list_number=[]

            for number in range (index_el_1+1,index_el_2):
                new_list_number.append(list_number_attributes[number])

            temp_number = maths_list(new_list_number)

            for de in range(index_el_2-index_el_1+1):
                list_number_attributes.pop(index_el_1)

            list_number_attributes.insert(index_el_1,str(temp_number))

            new_list_number.clear()
        return maths_list (list_number_attributes)
    

    
    return quotes_math(math)



math_data= str(input('Введите математическое выражение: '))

#print (f'eval = {eval(math_data)}')
    

print(f'{math_data} = {math_str(math_data)}')
    
    



# numbers_new=maths_list(list_number_attributes)

# print(numbers_new)






