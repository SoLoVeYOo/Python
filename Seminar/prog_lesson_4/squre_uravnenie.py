# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

# a = input('Введите коэффициент A: ')
# b = input('Введите коэффициент B: ')
# c = input('Введите коэффициент C: ')

with open (r'Seminar\test_lesson_4\squreuravnenie.txt', 'r') as my_file:
    data = my_file.read()
data = data.replace('x^2','')
data = data.replace('x','')
data = data.split()
data = data[:-2]
a = data[0]
b = data[1]+data[2]
c = data[3]+data[4]
print(a, b, c)

def reshenie_math (a_in: float, b_in: float, c_in: float):
    diskriminant = b_in**2 - 4 * a_in * c_in
    if diskriminant > 0:
        result= {}
        result['первый корень'] = (-b_in + diskriminant**0.5) / (2 * a_in)
        result['второй корень'] = (-b_in - diskriminant**0.5) / (2 * a_in)
    elif diskriminant == 0: result = (-b_in) / (2 * a_in)
    else: result = 'У уравнения нет действительных корней'
    return result

try:
    a, b, c = float(a), float(b), float(c)
    print(f'Корнями квадратного уравнения {a}x^2 + {b}x + {c} = 0 является: {reshenie_math(a, b, c)}')
except: print('Ошибка! Введите действительные числа!')