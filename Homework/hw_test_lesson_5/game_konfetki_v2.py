# Создайте программу для игры с конфетами человек против человека.

import random

print('На столе лежит определенное количество конфеток. За раз можно брать от 1 до 28 конфетки.'
    'Победит тот, кто заберет последние конфетки со стола.')

rezim_game = input('Введите в какой режим хотите поиграть ("в двоем" или "с ботом"): ')
if rezim_game != 'с ботом' and rezim_game != 'в двоем':
    print('Запустите программу заного и укажите режим игры корректно!')
    exit()
col = input('Введите количество конфеток: ')
try: 
    col = int(col)
except:
    print('Запустите программу заного и укажите целое число конфеток!')
    exit()
if col <= 28:
    print('Введите большее количество конфеток!')
    exit()
chity = input('Включить подсказки? (да / нет): ')
if chity != 'да' and chity != 'нет':
    print('Запустите программу заного и введите верно ("да" или "нет"!')
    exit()

if rezim_game == 'в двоем':

    def game_with_player (konfetki: int, chit: str) -> str:
        while konfetki > 0:
            print(f'Осталось: {konfetki}')
            if chit == 'да':
                podskazka = konfetki%29
                if podskazka == 0: print(f'У второго игрока приемущество!')
                else: print(f'Подсказка: {podskazka}')
            player1 = int(input('Сколько конфеток берете? (от 1 до 28): '))
            konfetki -= player1
            if konfetki == 0:
                return 'Игрок 1 Победил!'
                break
            print(f'Осталось: {konfetki}')
            player2 = int(input('Сколько конфеток берете? (от 1 до 28): '))
            konfetki -= player2
            if konfetki == 0:
                return 'Игрок 2 Победил!'
                break

    print(game_with_player(col, chity))

if rezim_game == 'с ботом':
    difficulty = int(input('Выберите сложность от 0 до 10, где 0 - "не интересно", а 10 - "у тебя нет права на ошибку!": '))
    if difficulty < 0 or difficulty > 10:  
        print('Запустите программу заного и введите верно уровень сложности!')
        exit()

    def game_with_com (konfetki: int, chit: str, diff: int) -> str:
        while konfetki > 0:
            print(f'Осталось: {konfetki}')
            if chit == 'да':
                podskazka = konfetki%29
                if podskazka == 0: print(f'У компьютера приемущество!')
                else: print(f'Подсказка: {podskazka}')
            player1 = int(input('Сколько конфеток берете? (от 1 до 28): '))
            if player1 < 1 or (player1 > 28 and player1 != konfetki):
                print(f'Компьютер говорит: "Ты жульничаешь! Я тоже буду! God mod = ON!"')
                diff = 11
            elif player1 == konfetki and player1 > 28:
                print(f'Компьютер говорит: "Ты жульничаешь! С жуликами не играю!"')
                exit()
            konfetki -= player1
            if konfetki == 0:
                return 'Игрок Победил!'
                break
            print(f'Осталось: {konfetki}')
            if 0 <= diff <= 10:
                bot = random.choices([int(random.randint(1, 28)), int(konfetki % 29)], weights=[100-diff*10, diff*10])
                if bot[0] == 0: bot[0] = random.randint(1, 28)
            else: bot = random.choices([int(konfetki), int(konfetki % 29)], weights=[10, 90])
            print(f'Компьютер берет: {bot[0]}')
            konfetki -= bot[0]
            if konfetki == 0:
                return 'Компьютер Победил!'
                break

    print(game_with_com(col, chity, difficulty))