# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

from turtle import pos

a = input('Введите первую строку: ')
b = input('Введите вторую строку: ')

def poisk_sovpadeniy(stroka1, stroka2):
    shetchik = 0
    for i in range(len(stroka1) - len(stroka2)+1):
        if stroka2 == stroka1[i: i + len(stroka2)]: shetchik += 1
    return shetchik

def poisk_sovpadeniy2(stroka1, stroka2):
    position = 0
    shetchik = 0
    while (True):
        position = stroka1.find(stroka2, position)
        if position == -1: break
        else:
            position+= len(stroka2)
            shetchik+=1
    return shetchik

def poisk_sovpadeniy3(stroka1, stroka2):
    shetchik = stroka1.count(stroka2)
    return shetchik   

print(poisk_sovpadeniy(a, b))
print(poisk_sovpadeniy2(a, b))
print(poisk_sovpadeniy3(a, b))