import random
def congratulation(file_name):
    try:
        with open(file_name, encoding='utf-8') as file:
            con = file = file.readlines()
        if con: #Проверка на пустой фаил
            print(random.choice(con))
        else:
            print('Фаил пустой')
    except FileNotFoundError:
        print(f'Фаил не найден {file_name}')
    except Exception as e:
        print(f"Неизвестная ошибка {e}")

congratulation("congrats.txt")
