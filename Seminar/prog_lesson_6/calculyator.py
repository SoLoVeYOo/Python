# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный. 

# - Добавьте возможность использования скобок, меняющих приоритет операций.
import string

primer = input('Введите уравнение: ')

operacii = ['/', '*', '-', '+']

def sort_primer (stroka: str) -> list:
    result, temp_str = [], ''
    if stroka[0] == '-': temp_str, stroka = '-', stroka[1:]
    for i in range(len(stroka)):
        if stroka[i].isdigit() == True or stroka[i] == '.': temp_str += stroka[i]
        elif stroka[i] in operacii:
            result.append(float(temp_str))
            result.append(stroka[i])
            temp_str = ''
        if i+1 == len(stroka): result.append(float(temp_str))
    return result

def calc(spisok: list) -> float:
    for oper in operacii:
        while oper in spisok:
            for i in range(len(spisok)):
                prov = False
                if oper == spisok[i]:
                    match oper:
                        case '/': res = spisok[i-1] / spisok[i+1]
                        case '*': res = spisok[i-1] * spisok[i+1]
                        case '-': res = spisok[i-1] - spisok[i+1]
                        case '+': res = spisok[i-1] + spisok[i+1]
                    spisok.insert(i-1, res)
                    del spisok[i]
                    del spisok[i]
                    del spisok[i]
                    prov = True
                if prov == True: break 
        if len(spisok) == 1: break
    return spisok[0]

print(calc(sort_primer(primer)))



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