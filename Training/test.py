def open_history(filelog):
    try:
        with open(filelog) as file:
            log = file.read()
            print(log)
    except FileNotFoundError:(
        print(f"Фаил {filelog} не найден"))
    except Exception as e:
        print(f"Ошибка чтения из файла {e}")

open_history("calk_log.txt")

# with open(file_name, encoding='utf-8') as file:
#     con = file = file.readlines()
# if con:  # Проверка на пустой фаил
#     print(random.choice(con))