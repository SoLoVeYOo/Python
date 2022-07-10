# Немного о строках

text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39 - количество символов
print('ещё' in text) # True - проверка наличия подстроки в строке
print(text.isdigit()) # False - являются ли все строки числами
print(text.islower()) # True  - являются ли все строки нижним регистром
print(text.replace('ещё','ЕЩЁ')) # - замена

for c in text:
    print(c)

help(text.title) # - запрос помощи что делает та или иная команда

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...