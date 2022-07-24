# Вычислить число c заданной точностью d

d = input('Введите заданную точность: ')

def vychislenie_pi (tochnost: str) -> str:
    tochnost, summa = len(tochnost[2:]), 1
    for i in range(1, 1000000):
        summa += (((-1)**i) / (2 * i + 1))
    pi = str(summa * 4)[0:tochnost+2]
    return pi

try:
    proverka = float(d)
    print(f'Число Pi с заданной точностью {float(d)}: {vychislenie_pi(d)}')
except: print('Ошибка! Введите правильную точность!')