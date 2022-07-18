# Напишите простой калькулятор, который считывает с пользовательского 
# ввода три строки: первое число, второе число и операцию, после чего 
# применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

vvodnoe = input('Введите уравнение: ')

def calculator (stroka: str) -> float:
    stroka.replace(' ', '')
    slovar = ['+', '-', '/', '*', 'mod', 'pow', 'div']
    for i in slovar:
        if stroka.find(i) != -1:
            operaciya = i
            break
        else: operaciya = False
    if operaciya == False: print('Данные введены неверно')
    else: 
        temp = stroka.split(operaciya)
        x1 = temp[0]
        x2 = temp[1]
        try:
            x1 = float(x1)
            x2 = float(x2)
            proverka = x1 / x2
            match operaciya:
                case '+': return x1 + x2
                case '-': return x1 - x2
                case '/': return x1 / x2
                case '*': return x1 * x2
                case 'mod': return x1 % x2
                case 'pow': return x1 ** x2
                case 'div': return x1 // x2
        except: print('Ошибка! Деление на 0')

print(f'{vvodnoe} = {calculator(vvodnoe)}')