# Неупорядоченные коллекции произвольных
# объектов с доступом по ключу

dictionary = {}
dictionary = \
    {
    'up': '↑',
    'left': '←',
    'down': '↓',
    'right': '→'
    }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться

print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

for k in dictionary.keys(): # ключи
    print(k)

for v in dictionary.values(): # значения словаря
    print(v)

for k, v in dictionary.items(): # ключи и значения словаря
    print(k,v)

print(type(dictionary))