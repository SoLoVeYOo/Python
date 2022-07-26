import random
def sluchaynyy_mnogochlen (k: int) -> str:
    stroka = ''
    if k == 3:
        a = random.randint(1, 5)
        if a == 0: stroka += ''
        elif a == 1: stroka += f'1x^3'
        else: stroka += f'{a}x^3' 
    if k >= 2:
        if k == 2: b = random.randint(1, 5)
        else: b = random.randint(0, 5)
        if b == 0: stroka += ''
        elif b == 1: stroka += f' + 1x^2'
        else: stroka += f' + {b}x^2'
    if k >= 1:
        if k == 1: d = random.randint(1, 5)
        else: d = random.randint(0, 5)
        if d == 0: stroka += ''
        elif d == 1: stroka += f' + 1x'
        else: stroka += f' + {d}x'
    c = random.randint(0, 5)
    if c == 0: stroka += ''
    else: stroka += f' + {c}'
    stroka += ' = 0'
    if k != 3: stroka = stroka[3:]
    return stroka