import json

from nbformat.corpus import words
from openpyxl.chart import title

with open('dict.json', 'r', encoding='utf-8') as file:
    d = json.load(file)

while True:

    word = input('Введите слово для перевода:').strip().lower()
    if word in d:
        print(f'{word.title()} - {(d[word]).title()}')
    elif word == 'exit':
        break
    else:
        translete = input(f'Введите перевод {word}:').strip().lower()
        d[word] = translete
        with open('dict.json', 'w', encoding='utf-8') as file:
            json.dump(d, file, indent=4)



# with open('dict.json', 'w', encoding='utf-8') as file:
#     json.dump(d, file, indent=4)