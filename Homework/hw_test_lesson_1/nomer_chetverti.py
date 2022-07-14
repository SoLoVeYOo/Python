# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = float(input('Введите координаты X: '))
y = float(input('Введите координаты Y: '))

if x > 0 and y > 0: print('I четверть')
elif x < 0 and y > 0: print('II четверть')
elif x < 0 and y < 0: print('III четверть')
elif x > 0 and y < 0: print('IV четверть')
elif x == 0 and y != 0: print('Точка находится на оси Y')
elif y == 0 and x != 0: print('Точка находится на оси X')
else: print('Точка находится в центре координат')