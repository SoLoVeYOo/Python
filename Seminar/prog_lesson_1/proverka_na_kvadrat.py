# Написать программу которая будет принимать на вход два числа
# и будет проверять не является ли одно число квадратом другого

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def proverka(x, y):
    if y == x*x: print(f'число {y} является квадратом числа {x}')
    elif x == y*y: print(f'число {x} является квадратом числа {y}')
    else: print('числа не являются квадратми друг друга')

proverka(a,b)