
import random
print('На столе лежит определенное количество конфеток. За раз можно брать от 1 до 28 конфетки.'
    'Победит тот, кто заберет последние конфетки со стола.')
rezim_game = input('Введите в какой режим хотите поиграть (в двоем или с компьютером): ')
col = int(input('Введите количество конфеток: '))
chity = input('Включить помощь? : ')

if rezim_game == 'в двоем':

    def game_with_player (konfetki: int, chit: str) -> str:
        while konfetki !=0:
            print(f'Осталось: {konfetki}')
            if chit == 'да':
                podskazka = konfetki%29
                if podskazka == 0: print(f'У второго игрока приемущество!')
                else: print(f'Подсказка: {podskazka}')
            player1 = int(input('Сколько конфеток берете?: '))
            konfetki -= player1
            if konfetki == 0:
                return 'Player 1 WIN!'
                break
            print(f'Осталось: {konfetki}')
            player2 = int(input('Сколько конфеток берете?: '))
            konfetki -= player2
            if konfetki == 0:
                return 'Player 2 WIN!'
                break

    print(game_with_player(col, chity))

if rezim_game == 'с компьютером':
    difficulty = int(input('Выберите сложность от 0 до 10, где 0 - легко, а 10 - одна ошибка и проигрыш: '))

    def game_with_com (konfetki: int, chit: str, diff: int) -> str:
        while konfetki !=0:
            print(f'Осталось: {konfetki}')
            if chit == 'да':
                podskazka = konfetki%29
                if podskazka == 0: print(f'У компьютера приемущество!')
                else: print(f'Подсказка: {podskazka}')
            player1 = int(input('Сколько конфеток берете?: '))
            konfetki -= player1
            if konfetki == 0:
                return 'Player WIN!'
                break
            print(f'Осталось: {konfetki}')
            random.choices(['Катя', 'Коля'], weights=[10, 20])
            bot = random.choices([int(random.randint(1, 28)), int(konfetki % 29)], weights=[100-diff*10, diff*10])
            if bot[0] == 0: bot[0] = random.randint(1, 28)
            print(f'Компьютер берет: {bot[0]}')
            konfetki -= bot[0]
            if konfetki == 0:
                return 'Computer WIN!'
                break

    print(game_with_com(col, chity, difficulty))