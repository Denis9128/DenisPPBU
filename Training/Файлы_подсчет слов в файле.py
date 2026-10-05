def count(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            countent = file.read()
            word = countent.split()
            return len(word)
    except FileNotFoundError:
        print("Фаил не найден")
    except Exception as e:
        print(f"Произошла ошибка{e}")

word = count("proba.txt")
print(f"Количество слов в файле: {word}")
