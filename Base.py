from random import randint, random

def check_number ( text_in:str = 'Введите число: ', text_breac:str = 'Вы ввели число не правильно, введите его заново:'): 
    '''
    Проверка, явл.ется ли введённые данные числом. 
    Если нет то повторяется запрос заново.
    text_in - техт запроса в консоли
    text_breac - техт вторичного запроса, при неправильном вводе числа
    '''
    while True:
        try:
            number = float(input(text_in))
            return number
    
        except ValueError:
            print(text_breac)


def check_number_min ( min_number:int = 0, text_in:str = 'Введите число: ', text_breac:str = 'Вы ввели число не правильно, введите его заново:', text_min:str ='Вы ввели число меньше минимального, введите его заново: '): 
    '''
    Проверка, являются ли введённые данные числом и не меньше минимума. 
    Если нет то повторяется запрос заново.
    text_in - техт запроса в консоли
    text_breac - техт вторичного запроса, при неправильном вводе числа
	text_min - текст запроса, если число меньше минимума
	min_number - минимальное число


    '''
    while True:
        try:
            number = float(input(text_in))

            if number<min_number:
                print(text_min)
                continue
            return number
    
        except ValueError:
            print(text_breac)

def check_number_min_max ( min_number:int = 0, max_number: int =100, text_in:str = 'Введите число: ', text_breac:str = 'Вы ввели число не правильно, введите его заново:', text_min:str ='Вы ввели число меньше минимального, введите его заново: ', text_max:str ='Вы ввели число больше максимального, введите его заново: '): 
    '''
    Проверка, являются ли введённые данные числом, и лежит ли это число в диапазоне 
    от минимума до максимума. 
    Если нет то повторяется запрос заново.
    text_in - техт запроса в консоли
    text_breac - техт вторичного запроса, при неправильном вводе числа
	text_min - текст запроса, если число меньше минимума
	text_max - текст запроса, если число больше максимума
	min_number - минимальное число
 	max_number - максимальное число
    '''
    while True:
        try:
            number = float(input(text_in))

            if number<min_number:
                print(text_min)
                continue
            if number>max_number:
                print(text_max)
                continue
            return number
    
        except ValueError:
            print(text_breac)








def random_list_number ( rendg_:int,min_:int, max_:int):
    '''
    Заполнение списка случайными числами
    rendg_ - длина списка
    min_ - минимальное значение случайной величины
    max_ - максимальное значение случайной величины

    '''
    list_my = []

    for i in range(0,rendg_):
        list_my.append(randint(min_,max_))
    
    return list_my


def prime_number (number_new:int):
    '''
    Функция, которая находит следующее простое число. 
    Простое число, это число которое делится только на 1 или на само себя без остатка, 
    на все остальные делиться с остатком.
    '''
    def prime_number_number (number):
        if number ==2:
            return 3
        elif number >= 3:
            number +=2
            while   number  %3 ==0 or (round(number**0.5,0)**2==number) :
                number +=2

        return number
    number_new=prime_number_number (number_new)

    if number_new==3 or number_new==5:
        return number_new
    number1=5
    while number1*prime_number_number(number1)<=number_new or number_new//number1*number1>=number_new or  number_new  %3 ==0 or number_new%5==0:
        if number1*prime_number_number(number1)==number_new or number_new//number1*number1==number_new or number_new  %3 ==0 or number_new%5==0:
            number_new+=2
           
        else:
            number1=prime_number_number(number1)
    

    return number_new


def encoder_caesar(text:str,key:int):
    '''
    Кодирование по "Шифру Цезаря", смещение каждой буквы происходит в лево или право по алфавиту
    на определённое количество символов. Смещение зависит от ключа.
    text - шифруемый текст
     key - ключ шифрования, если ключ положительный, то происходит смешение в лево,
            если отрицательный то смещение в право.
    '''
    dictionary_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    dictionary_ru_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    dictionary_en= "abcdefghijklmnopqrstuvwxyz"
    dictionary_en_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_text =''
    for letter in text:
        if dictionary_ru.find(letter)>-1:
            new_text+=dictionary_ru[(dictionary_ru.find(letter)+key)%32]
        elif dictionary_ru_upper.find(letter)>-1:
            new_text+=dictionary_ru_upper[(dictionary_ru_upper.find(letter)+key)%32]
        elif dictionary_en.find(letter)>-1:
            new_text+=dictionary_en[(dictionary_en.find(letter)+key)%25]
        elif dictionary_en_upper.find(letter)>-1:
            new_text+=dictionary_en_upper[(dictionary_en_upper.find(letter)+key)%25]
        else:
            new_text+=letter
    return new_text

def decoder_caesar(text:str,key:int):
    '''
    Декодирование по "Шифру Цезаря", смещение каждой буквы происходит в лево или право по алфавиту
    на определённое количество символов. Смещение зависит от ключа.
    text - декодируемый текст
    key - ключ декодирования, если ключ отрицательный то происходит смешение в лево,
         если положительный то смещение в право.
    '''
    dictionary_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    dictionary_ru_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    dictionary_en= "abcdefghijklmnopqrstuvwxyz"
    dictionary_en_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_text =''
    for letter in text:
        if dictionary_ru.find(letter)>-1:
            new_text+=dictionary_ru[(dictionary_ru.find(letter)-key)%32]
        elif dictionary_ru_upper.find(letter)>-1:
             new_text+=dictionary_ru_upper[(dictionary_ru_upper.find(letter)-key)%32]
        elif dictionary_en.find(letter)>-1:
            new_text+=dictionary_en[(dictionary_en.find(letter)-key)%25]
        elif dictionary_en_upper.find(letter)>-1:
             new_text+=dictionary_en_upper[(dictionary_en_upper.find(letter)-key)%25]
        else:
            new_text+=letter
    return new_text


