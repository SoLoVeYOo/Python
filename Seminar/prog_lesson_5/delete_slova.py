# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'абв абв2 ва ываы ыавыв авб вабв выфв'

def delete_words (text_in):
    text_in = filter(lambda x: 'абв' not in x, text_in.split())
    return ' '.join(text_in)

print(delete_words(text))