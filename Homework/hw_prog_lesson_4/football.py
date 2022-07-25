# Напишите программу, которая принимает на стандартный вход
# список игр футбольных команд с результатом матча и выводит
# на стандартный вывод сводную таблицу результатов всех матчей.

team = {}
spartak = [0, 0, 0 ,0 ,0]
team['Спартак'] = spartak
lokomotiv = [0, 0, 0 ,0 ,0]
team['Локомотив'] = lokomotiv
zenit= [0, 0, 0 ,0 ,0]
team['Зенит'] = zenit
print(team)

while True:
    game = []
    for i in input('Введите резуьтат игры (team gol team gol) через пробел: ').split():
            game.append(i)

    def rezultat_matcha ():
        if game[0] == 'Спартак':
            spartak[0] += 1
            if game[1] < game[3]: spartak[3] += 1
            elif game[1] == game[3]:
                spartak[2] += 1
                spartak[4] += 1
            else:
                spartak[1] += 1
                spartak[4] += 3
        if game[0] == 'Локомотив':
            lokomotiv[0] += 1
            if game[1] < game[3]: lokomotiv[3] += 1
            elif game[1] == game[3]:
                lokomotiv[2] += 1
                lokomotiv[4] += 1
            else:
                lokomotiv[1] += 1
                lokomotiv[4] += 3
        if game[0] == 'Зенит':
            zenit[0] += 1
            if game[1] < game[3]: zenit[3] += 1
            elif game[1] == game[3]:
                zenit[2] += 1
                zenit[4] += 1
            else:
                zenit[1] += 1
                zenit[4] += 3

    rezultat_matcha()
    game[0], game[1], game[2], game[3] = game[2], game[3], game[0], game[1] # разворачиваем результат матча, чтобы проверить данные по второй команде
    rezultat_matcha()
    print(team)

    if input('Еще игра?: ') == 'нет': break