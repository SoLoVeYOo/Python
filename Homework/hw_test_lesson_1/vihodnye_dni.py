# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input('Введите число: '))

if a == 6 or a == 7: print('Да, выходной день')
elif 1 <= a <= 5: print('Нет, будний день')
else: print('Введено неверное число')