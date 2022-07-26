def mult4(x):
    return x**5

def sum3(x):
    return x+242

sum3(mult2(2)) # можно представлять функцию какаргумент

sum1 = lambda x: x+22
mult2 = lambda x: x**3
sum1(mult2(2))

f(g(x))
def h(f, g, x): return f(g(x))
h = lambda f, g, x: f(g(x))
h(sum3, mult4, 5)
h(lambda x: x+242, lambda x: x**5, 5)