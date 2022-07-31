# Создайте программу для игры в "Крестики-нолики"

# В процессе разработки решил что проще составить
# список с выйграшными вариантами:
# if pole[0] == pole[1] == pole [2]: win
# if pole[3] == pole[4] == pole [5]: win
# if pole[6] == pole[7] == pole [8]: win
# if pole[0] == pole[3] == pole [6]: win
# if pole[1] == pole[4] == pole [7]: win
# if pole[2] == pole[5] == pole [8]: win
# if pole[0] == pole[4] == pole [8]: win
# if pole[6] == pole[4] == pole [2]: win

# spisok_win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [6,4,2]]

pole = list(range(1,10))

def generacia_polya(pole): # для представления списка pole как доски
    print()
    for i in range(3):
        print (pole[0+i*3], "|", pole[1+i*3], "|", pole[2+i*3])
        if i < 2: print("-" * 9)
        else: print()

def vvod_igrakov(simvol):
    temp = False
    while not temp:
        hod_igroka = input("Куда поставите " + simvol+"?: ")
        try: hod_igroka = int(hod_igroka)
        except:
            print ("Ошибка! Введите целое число!")
            continue
        if 1 <= hod_igroka <= 9:
            if (str(pole[hod_igroka-1]) not in "X0"): pole[hod_igroka-1], temp = simvol, True
            else: print ("Эта клеточка уже занята")
        else: print ("Ошибка! Введите число от 1 до 9!")

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
        if count % 2 == 0: vvod_igrakov("X")
        else: vvod_igrakov("0")
        count += 1
        if count > 4: # до 5 хода никто победить не может
            temp = proverka(pole)
            if temp:
                print (f'Игрок с {temp} победил!')
                win = True
                break
        if count == 9:
            print ("Ничья!")
            break
    generacia_polya(pole)

game(pole)