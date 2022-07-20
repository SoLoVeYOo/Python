# Задайте список из n чисел ряда фибоначчи

n = input('Введите целое число: ')
a1 = input('Введите первое число: ')
a2 = input('Введите второе число: ')

# n = int(input('Введите целое число: '))
# a1 = int(input('Введите первое число: '))
# a2 = int(input('Введите второе число: '))

def fibonachi (f: int, a: int, b: int) -> list:
    fib = []
    fib.append(a)
    fib.append(b)
    for i in range(f):
        element = a + b
        fib.append(element)
        a, b = b, element
    return fib

def fibonachi_recursion (f: int) -> int:
    if f == 1 or f == 2: return 1
    else: return fibonachi_recursion(f-1)+fibonachi_recursion(f-2)

def fibonachi_recursion_list(f: int) -> list:
    spisok = []
    for i in range(1, f+1):
        spisok.append(fibonachi_recursion(i))
    return spisok

try:
    n = int(n)
    a1 = int(a1)
    a2 = int(a2)
    print(fibonachi(n, a1, a2))
    print(fibonachi_recursion_list(n))
except: print('Введите целые числа')