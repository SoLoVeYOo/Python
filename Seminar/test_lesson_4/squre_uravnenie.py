# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

from cmath import sqrt

a = input('Введите коэффициент A: ')
b = input('Введите коэффициент B: ')
c = input('Введите коэффициент C: ')

def reshenie_math (a_in: float, b_in: float, c_in: float):
    diskriminant = b_in**2 - 4 * a_in * c_in
    if diskriminant < 0: result = 'У уравнения нет действительных корней'
    if diskriminant == 0:
        result = (-b_in) / (2 * a_in)
    if diskriminant > 0:
        x1 = (-b_in + sqrt(diskriminant)) / (2 * a_in)
        x2 = (-b_in - sqrt(diskriminant)) / (2 * a_in)
        result= {}
        result['первый корень'] = x1
        result['второй корень'] = x2
    return result

try:
    a = float(a)
    b = float(b)
    c = float(c)
    print(f'Корнями квадратного уравнения {a}x^2 + {b}x + {c} = 0 является: {reshenie_math(a, b, c)}')
except: print('Ошибка! Введите действительные числа!')