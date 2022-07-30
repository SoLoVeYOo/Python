# Напишите программу, удаляющую из текста все слова, содержащие "абв".

with open(r'Homework\hw_test_lesson_5\delete_slova.txt','r', encoding='utf-8') as my_file:
        my_text = my_file.read()
print(my_text)

def delete_words (text_in):
    text_out = filter(lambda x: 'абв' not in x, text_in.split())
    return ' '.join(text_out)

print(delete_words(my_text))

text = ' '.join([i for i in my_text.split() if 'абв' not in str(i)])
print(text)