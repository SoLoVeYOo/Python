# Напишите программу которая принимает на вход 5 чисел и находит большее из них

a1 = int(input('Введите первое число: '))
a2 = int(input('Введите второе число: '))
a3 = int(input('Введите третье число: '))
a4 = int(input('Введите четвертое число: '))
a5 = int(input('Введите пятое число: '))


def find_bigest(b1, b2, b3, b4, b5):
    max = b1
    for i in b2, b3, b4, b5:
        if i > max: max = i
    return max


print(f'Максимально число: {find_bigest(a1,a2,a3,a4,a5)}')

# chisla = list(input('Введите числа через запятую: '))


# def find_bigest(ls):
#     max = ls[0]
#     for i in ls:
#         if i > max: max = i
#     return max

# print(f'Максимально число: {find_bigest(chisla)}')
