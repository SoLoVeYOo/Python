import random

def create_uravnenie():
    k = int(input('Введите коэфициент: '))
    koef = [random.randint(0, 5) for _ in range(k+1)]

    def soisok_chlenov (koe) -> list:
        spisok = []
        for (s, k) in list(enumerate(koe)):
            if k != 0:
                if s == 0: spisok.append(f'{k}')
                elif s == 1: spisok.append(f'{k}x')
                else: spisok.append(f'{k}x^{s}')
        return spisok
    uravnenie = ' + '.join(soisok_chlenov(koef)[::-1]) + ' = 0'
    return uravnenie