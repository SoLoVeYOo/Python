# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный. 

# - Добавьте возможность использования скобок, меняющих приоритет операций.
import string

primer = input('Введите уравнение: ')

result = []
temp = ''
for i in range(len(primer)):
    if primer[i].isdigit() == True or primer[i] == '.':
        temp += primer[i]
    elif primer[i] in ['*', '/', '+', '-']:
        result.append(float(temp))
        result.append(primer[i])
        temp = ''
    if i+1 == len(primer):
        result.append(float(temp))
print(result)
slovar = ['/', '*', '-', '+']
b = False
a = False
while b == False:
    for oper in slovar:
        while oper in result:
            for i in range(len(result)):
                if oper == result[i]:
                    match oper:
                        case '/': temp = result[i-1] / result[i+1]
                        case '*': temp = result[i-1] * result[i+1]
                        case '+': temp = result[i-1] + result[i+1]
                        case '-': temp = result[i-1] - result[i+1]
                    print(temp)
                    result.insert(i-1, temp)
                    del result[i]
                    del result[i]
                    del result[i]
                    print(result)
                    a = True
                if a == True:
                    a = False
                    break 
        if len(result) == 1:
            b = True
            break
print(result)




# def calculator (stroka: str) -> float:
#     stroka.replace(' ', '')
#     slovar = ['+', '-', '/', '*', 'mod', 'pow', 'div']
#     for i in slovar:
#         if stroka.find(i) != -1:
#             operaciya = i
#             break
#         else: operaciya = False
#     if operaciya == False: print('Данные введены неверно')
#     else: 
#         temp = stroka.split(operaciya)
#         x1 = temp[0]
#         x2 = temp[1]
#         try:
#             x1 = float(x1)
#             x2 = float(x2)
#             proverka = x1 / x2
#             match operaciya:
#                 case '+': return x1 + x2
#                 case '-': return x1 - x2
#                 case '/': return x1 / x2
#                 case '*': return x1 * x2
#                 case 'mod': return x1 % x2
#                 case 'pow': return x1 ** x2
#                 case 'div': return x1 // x2
#         except: print('Ошибка! Деление на 0')

# print(f'{vvodnoe} = {calculator(vvodnoe)}')