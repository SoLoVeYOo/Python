# Напишите алгоритм задания случайных чисел без использования
# встроенного генератора псевдослучайных чисел

# import random
# random_list.append(random.random())

# import time
# n = int(input('Введите длину числа: '))
# temp = int(((time.time() % 1)* (10**(n+1))) % (10**(n))
# print(temp)

# def random_chisla (a: int) -> list:
#     random_list = []
#     for i in range(a):
#         temp = int(((time.time()%1)*1000)%100)
#         random_list.append(temp)
#     return random_list
# print(random_chisla(n))

# from time import time
# def time_random():
#  return time() - float(str(time()).split('.')[0])
# def gen_random_range(min, max):
#  return int(time_random() * (max - min) + min)
# if __name__ == '__main__':
#  for i in range(20):
#      print(gen_random_range(20,60))

# def randint(a, b):
#     "Return random integer in range [a, b], including both end points."
#     return a + randbelow(b - a + 1)
# def randbelow(n):
#     "Return a random int in the range [0,n).  Raises ValueError if n<=0."
#     # from Lib/random.py
#     if n <= 0:
#        raise ValueError
#     k = n.bit_length()  # don't use (n-1) here because n can be 1
#     r = getrandbits(k)          # 0 <= r < 2**k
#     while r >= n: # avoid skew
#         r = getrandbits(k)
#     return r
# print(*[randint(10, 110) for _ in range(20)])