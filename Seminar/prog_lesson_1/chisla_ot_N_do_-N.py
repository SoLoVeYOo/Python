# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

a = input('Введите число: ')

def chisla2(x):
    for i in range(-x, x+1):
        print(i, end=' ')

# def chisla(x):
#     i = -x
#     while i <= x:
#         print(i)
#         i += 1

try:
    a = int(a)
    chisla2(a)
except: print('Введите целое число')