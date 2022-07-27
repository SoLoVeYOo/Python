from random import randint

def GenerateTerms(coef: int, pow: int) -> str:
    if pow == 0:
        return f"{coef}"
    elif pow == 1:
        return f"{coef}*x"
    else:
        return f"{coef}*x^{pow}"

def Fun(k):
    coefficients = [randint(0, 3) for _ in range(k+1)]
    # print(coefficients)
    terms = [GenerateTerms(c, p) for (p, c) in enumerate(coefficients) if c != 0]
    print(terms)
    return " + ".join(terms[::-1]) + " = 0"

try:
    k = int(input("Введите степень многочлена (натуральное число): "))
    if k <= 0:
        raise
except:
    print("Нужно было ввести натуральное число.")
else:
    result = Fun(k)
    print(result)
    with open(r'Seminar\prog_lesson_5\file2.txt', "w") as f:
        f.write(result)