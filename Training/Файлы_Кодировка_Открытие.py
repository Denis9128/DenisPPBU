try:
    with open("proba.txt", encoding="utf-8") as file: # Кодировка
        content = file.read()
        print(content)

except FileNotFoundError:
    print('Фаил не найден')
