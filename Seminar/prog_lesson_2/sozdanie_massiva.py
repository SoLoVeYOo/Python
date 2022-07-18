# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

a = int(input('Введите чиcло: '))
b = int(input('Введите чиcло: '))

def sozdanie_massiva(x: int, y: int) -> list:
    chisla = [1]
    for i in range(1, x):
        chisla.append(chisla[-1]*y)
    return chisla

print(sozdanie_massiva(a, b))