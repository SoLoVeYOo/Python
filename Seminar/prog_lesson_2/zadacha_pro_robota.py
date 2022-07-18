#В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу, 
# по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".
# Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.
# Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное), выводящее это число в консоль 
# вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с людьми, 
# например: 1 программист, 2 программиста, 5 программистов.
# В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи,
# как минимум до 1000 человек.

n = input('Колличество программистов: ')

def robot_speak(number: int):
    if number >= 0:
        number = str(number)
        if int(number[len(number)-1]) == 1 and int(number) != 11 : print(f'В комнате {number} программист')
        if 2 <= int(number) <= 4 or 2 <= int(number[len(number)-1]) <= 4 and 4 <= int(number) and int(number) > 14 : print(f'В комнате {number} программиста')
        if 5 <= int(number) <= 14 or 5 <= int(number[len(number)-1]) <= 9 or int(number[len(number)-1]) == 0: print(f'В комнате {number} программистов')
    else: print('Введите неотрицательное число')

def robot_speak2(number: int):
    if number >= 0:
        if number % 10 == 1 and number != 11: print(f'В комнате {number} программист')
        if 2 <= number <= 4 or 2 <= number % 10 <= 4 and 4 <= number and number > 14: print(f'В комнате {number} программиста')
        if 5 <= number <= 14 or 5 <= number % 10 <= 9 or number % 10 == 0: print(f'В комнате {number} программистов')
    else: print('Введите неотрицательное число')

def robot_speak3(number: int):
    if number >= 0:
        if number % 10 == 1 and number != 11: return 'программист'
        if 2 <= number <= 4 or 2 <= number % 10 <= 4 and 4 <= number and number > 14: return 'программиста'  
        if 5 <= number <= 14 or 5 <= number % 10 <= 9 or number % 10 == 0: return 'программистов'  
    else: print('Введите неотрицательное число')

try:
    n = int(n)
    robot_speak(n)
    robot_speak2(n)
    print(f'В комнате {n} {robot_speak3(n)}')
except: print('Введите целое число')