# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

a = int(input('Введите чиcло: '))
b = int(input('Введите чиcло: '))

# def sozdanie_massiva(x: int, y: int) -> list:
#     chisla = [1]
#     for i in range(1, x):
#         chisla.append(chisla[-1]*y)
#     return chisla

# print(sozdanie_massiva(a, b))

def sozdanie_massiva(x): # без списка
    chisla = 1
    print(chisla, end=' ')
    for i in range(1, x):
        chisla *= (-3)
        print(chisla, end=' ')

sozdanie_massiva(a)