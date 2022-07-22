# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

chislo = input('Введите целое число: ')

def fibonacci_otr(chislo_in):
    spisok = []
    a, b = 1, 1
    for i in range(chislo_in):
        spisok.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (chislo_in+1):
        spisok.insert(0, a)
        a, b = b, a - b
    return spisok

try:
    chislo = int(chislo)
    print(fibonacci_otr(chislo))
except: print('Ошибка! Введите целое число!')