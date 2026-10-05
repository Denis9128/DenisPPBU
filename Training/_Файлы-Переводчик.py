def translate(filename):
    dictionary = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file: # 'r' открыть для чтения
            for line in file:
                key, value = line.split() # Делим на части строку
                dictionary[key] = value
            print(dictionary)

    except FileNotFoundError:
        print('Фаил не найден')
    except ValueError: # Ошибка формата словаря
        print("Ошибка формата словаря")
    except Exception as e:
        print(f"Неизвестная ошибка {e}")
    return dictionary

dikt= translate("dictionary.txt")
word = input("Введите слово: ")
if word in dikt:
    print(f"Перевод слова {word} - {dikt[word]}")
else:
    print("Слово не найдено")

