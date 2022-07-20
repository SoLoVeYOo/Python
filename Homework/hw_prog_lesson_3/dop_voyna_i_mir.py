# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его
# повторений (без учёта регистра) в формате "слово количество". Порядок вывода слов может быть произвольным, каждое уникальное
# слово должно выводиться только один раз.

text = input('Введите текст через пробел: ')
spisok = (text.lower()).split()
find_spisok = list(set(spisok))
print(spisok)
print(find_spisok)

# def uprochenie_spiska(iskomyy_spisok: list) -> list:
#     result_spisok = []
#     for i in iskomyy_spisok:
#         if i not in result_spisok: result_spisok.append(i)
#     return result_spisok

def poisk_sovpadeniy (iskomyy_spisok: list, poisk: list):
    for i in poisk:
        schetchik = 0
        for j in iskomyy_spisok:
            if j == i: schetchik +=1
        print(f'Колличество строк "{i}" в тексте равно: {schetchik}')

poisk_sovpadeniy (spisok, find_spisok)