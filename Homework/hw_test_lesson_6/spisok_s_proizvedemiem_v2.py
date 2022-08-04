# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.

number = input('Введите число ')
pozicii = [int(_) for _ in input('Введите позиции через пробел ').split()]

def sozdanie_spiska(chislo: int) -> list: return [-chislo+i for i in range(chislo*2+1)]
proiz = lambda x,y: x*y

try:
    number = int(number)
    spisok = sozdanie_spiska(number)
    print(spisok)
    print(f'Произведение чисел на позициях {pozicii} равно: {proiz(spisok[pozicii[0]], spisok[pozicii[1]])}')
except: print('Введите целое пложительное число!')   