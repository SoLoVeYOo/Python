# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

vvodnoe = input('Введите число: ')

def factorial (number: int) -> list:
    proizvedenie = 1
    result = []
    for i in range(1, number + 1):
        proizvedenie *= i
        result.append(proizvedenie) 
    return result

try:
    vvodnoe = int(vvodnoe)
    print(factorial(vvodnoe))
except: print('Введите целое число')