def write_to_fail(filename, data):
    try:
        with open(filename, "a") as file: # "a" Открыть фаил для добавления
            file.write(data + "\n")
            print("Данные ус пешно сохранены")
    except IOError:
        print("Ошибка при записи файла")

print("=Создатель дневника погоды=")
while True:
    data = input("Введите дату или слово 'выход' для заверщения: ")
    if data.lower() == 'выход':
        break
    t = input("Введите температуру: ")
    d = input("Осадки (да/нет)")
    data = f"{data}: Температура {t}, осадки {d}"

    write_to_fail("weather.txt", data)
