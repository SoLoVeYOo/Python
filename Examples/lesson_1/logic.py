# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# a = 1 < 4 and 5 > 2 # если хотя бы 1 условие не проходит - будет False
# a = 1 == 4 and 5 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# a = [1,2]
# b = [1,2]
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# z = 2
# print(func<T>z)

# f = 1 > 4 or 4 < 5 # дизбюнкция - если хотя бы 1 условие проходит - будет True
# print(f)

f =  [1,2,3,4]
print(f)
print(not 2 in f) # поиск в
iss_odd = f[0] % 2 == 0
iss_odd = not f[0] % 2 # аналогично выше
print(iss_odd)