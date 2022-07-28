
import random
print('На столе лежит определенное количество конфеток. За раз можно брать от 1 до 28 конфетки.'
    'Победит тот, кто заберет последние конфетки со стола.')
rezim_game = input('Введите в какой режим хотите поиграть (в двоем или с компьютером): ')
col = int(input('Введите количество конфеток: '))
chity = input('Включить : ')

def game (rezim_igry: str, konfetki: int) -> str:
    if rezim_igry == 'в двоем':
        while konfetki !=0:
            podskazka = konfetki%29
            if podskazka == 0: print(f'У второго игрока приемущество!')
            else: print(f'Подсказка: {podskazka}')
            player1 = int(input('Сколько конфеток берете?: '))
            konfetki -= player1
            if konfetki == 0:
                return win + 'Player 1 WIN!'
                break
            player2 = int(input('Сколько конфеток берете?: '))
            konfetki -= player1
            if konfetki == 0:
                return win + 'Player 2 WIN!'
                break
            print(f'Осталось: {konfetki}')
    if rezim_igry == 'с компьютером':
        while konfetki !=0:
            podskazka = konfetki%29
            if podskazka == 0: print(f'У компьютера приемущество!')
            else: print(f'Подсказка: {podskazka}')
            player1 = int(input('Сколько конфеток берете?: '))
            konfetki -= player1
            if konfetki == 0:
                return win + 'Player WIN!'
                break
            print(f'Осталось: {konfetki}')
            bot = konfetki % 29
            if bot == 0: bot = random.randint(1, 28)
            print(f'Компьютер берет: {bot}')
            konfetki -= bot
            if konfetki == 0:
                win = 'Computer'
                return win + ' WIN!'
                break
            print(f'Осталось: {konfetki}')

print(game(rezim_game, col))