def get_namber(prompt):
    while True: # Пока не будет введено целое число, будет просить ввести число заново
        value = input(prompt)
        if value.lstrip("-").isdigit(): # lstrip - Удаляет минус слева в строке
            return int(value)
        else:
            print("Это не целое число")

add = lambda x,y: x+y
subtract = lambda x,y: x-y
multiply = lambda x,y: x*y

def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return ("Ошибка! Деление на ноль.")
    except TypeError:
        return "Ошибка типа данных"

def log(rez): # Запись файла истории
    try:
        with open("calculations.txt","a") as logfile: # "a" - Открываем в режиме записи
            logfile.write(rez + "\n") # Записываем каждую строку с новой строки
    except FileNotFoundError:
        print(f"Фаил {rez}не найден")
    except Exception as e:
        print(f"Неизвестная ошибка {e}")


print("Выбирите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Просмотр истории вычислении")

# Проверяем на введенное число. Должно быть одно из укзанных в списке
valid_choices = ["1", "2", "3", "4","5"]
choice = None
while choice not in valid_choices:
    choice = input("Введите номер опереции: ")
    if choice not in valid_choices:
        print("Вы ввели не 1,2,3,4 или 5.")

if choice != "5": # Если не число 5, то вводим числа
    nam1 = get_namber("Введите первое число: ")
    nam2 = get_namber("Введите второе число: ")

def open_history(filelog): # Открываем фаил с иторией
    try:
        with open(filelog) as file:
            log = file.read()
            print(log)
    except FileNotFoundError:(
        print(f"Фаил {filelog} не найден"))
    except Exception as e:
        print(f"Ошибка чтения из файла {e}")


if choice == "1":
    rez = f"Результат: {nam1}+{nam2} = {add(nam1,nam2)}"
    print(rez)
elif choice == "2":
    rez = f"Результат: {nam1}-{nam2} = {subtract(nam1,nam2)}"
    print(rez)
elif choice == "3":
    rez = f"Результат: {nam1}*{nam2} = {multiply(nam1,nam2)}"
    print(rez)
elif choice == "4":
    result = divide(nam1,nam2)
    if isinstance(result,str): # isinstance - проверяем, относится ли данные result к строке
        rez = result
        print(rez)
    else:
        rez = f"Результат: {nam1}/{nam2} = {result:.2f}" # Оставляет 2 знака после запятой
        print(rez)

elif choice == "5":
    print("===История вычеслений===")
    open_history("calculations.txt")

if choice != "5": # Если не 5 операция, записываем действие в историю вызвав функцию log(), rez - передаём значение
    log(rez)








