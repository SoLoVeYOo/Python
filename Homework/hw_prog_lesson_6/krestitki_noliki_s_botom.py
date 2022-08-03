# Создайте программу для игры в "Крестики-нолики"

# spisok_win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [6,4,2]]
import random

pole = list(range(1,10))

def generacia_polya(pole): # для представления списка pole как доски
    print()
    for i in range(3):
        print (pole[0+i*3], "|", pole[1+i*3], "|", pole[2+i*3])
        if i < 2: print("-" * 9)
        else: print()

def vvod_igroka():
    temp = False
    while not temp:
        hod_igroka = input('Куда поставите "X"? ')
        try: hod_igroka = int(hod_igroka)
        except:
            print ("Ошибка! Введите целое число!")
            continue
        if 1 <= hod_igroka <= 9:
            if (str(pole[hod_igroka-1]) not in "X0"): pole[hod_igroka-1], temp = 'X', True
            else: print ("Эта клеточка уже занята")
        else: print ("Ошибка! Введите число от 1 до 9!")

def iq_computer (variant1: str, variant2: str, turn: int):
    spisok_win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [6,4,2]]
    temp = False
    if turn == 1:
        if pole[4] != 'X':
            print(f'Компьютер ставит "0" на {pole[4]} клетку')
            pole[4], temp = '0', True
        else:
            print(f'Компьютер ставит "0" на {pole[0]} клетку')
            pole[0], temp = '0', True
    else:
        for var in spisok_win:
            if (pole[var[0]] == pole[var[1]] == variant2) and (str(pole[var[2]]) != variant1):
                print(f'Компьютер ставит "0" на {pole[var[2]]} клетку')
                pole[var[2]], temp = '0', True
                break
            elif (pole[var[0]] == pole[var[2]] == variant2) and (str(pole[var[1]]) != variant1):
                print(f'Компьютер ставит "0" на {pole[var[1]]} клетку')
                pole[var[1]], temp = '0', True
                break
            elif (pole[var[1]] == pole[var[2]] == variant2) and (str(pole[var[0]]) != variant1):
                print(f'Компьютер ставит "0" на {pole[var[0]]} клетку')
                pole[var[0]], temp = '0', True
                break
    return temp


def vvod_computera(turn):
    temp = False
    while not temp:
        if iq_computer('X', '0', turn) == True:
            temp = True
            break
        elif iq_computer('0', 'X', turn) == True:
            temp = True
            break
        else:
            hod_comp = random.randint(1, 9)
            if (str(pole[hod_comp-1]) not in "X0"):
                print(f'Компьютер ставит "0" на {hod_comp} клетку')
                pole[hod_comp-1], temp = '0', True
        

def proverka(pole):
    spisok_win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [6,4,2]]
    for var in spisok_win:
        if pole[var[0]] == pole[var[1]] == pole[var[2]]:
            return pole[var[0]]
    return False

def game(pole):
    count = 0
    win = False
    while win == False:
        generacia_polya(pole)
        if count % 2 == 0: 
            vvod_igroka()
            temp = proverka(pole)
            if temp:
                print('Игрок победил!')
                win = True
                break
        else: 
            vvod_computera(count)
            temp = proverka(pole)
            if temp:
                print('Компьютер победил!')
                win = True
                break       
        count += 1
        if count == 9:
            print ("Ничья!")
            break
    generacia_polya(pole)

game(pole)