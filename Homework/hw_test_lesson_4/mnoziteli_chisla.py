# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

number = input('Введите целое число: ')

def spisok_mnoziteley(n):
   i = 2
   spisok = []
   while i * i <= n:
       while n % i == 0:
           spisok.append(i)
           n /= i
       i += 1
   if n > 1:
       spisok.append(int(n))
   return spisok

try:
    number = int(number)
    print(f'Список простых множителей числа {number}: {spisok_mnoziteley(number)}')
except: print('Ошибка! Введите целое число!')