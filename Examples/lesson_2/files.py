# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.write('\nLine 12\n')
# data.write('Line 13\n')
# data.close()

# with open('file.txt', 'w') as data: #не нужно вызывать закрытие файла
#     data.write('line 1243\n')
#     data.write('line 252352\n')

# exit() # закрывает программу принудительно и не выполяет код дальше

path = 'file.txt' # создаем путь к папке
data = open(path, 'r') # открываем в режиме чтения
for line in data:
    print(line)
data.close()

exit()