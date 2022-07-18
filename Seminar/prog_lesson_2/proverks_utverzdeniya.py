# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def proverka(a, b):
    for x in a, b:
        for y in a, b:
            for z in a, b:
                left = not (x or y or z)
                right = not (x) and not (y) and not (z)
                print(f'¬({x} ⋁ {y} ⋁ {z}) = {left}, ¬{x} ⋀ ¬{y} ⋀ ¬{z} = {right}')
                if left == right : print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} Истина')
                else: print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} Ложно')

proverka(True, False)