def get_namber(prompt):
    while True:
        value = input(prompt)
        if value.lstrip("-").isdigit(): # lstrip - Удаляет минус слева в строке
            return int(value)
        else:
            print("Это не целое число")

add = lambda x,y: x+y
subtract = lambda x,y: x-y
multiply = lambda x,y: x*y
divide = lambda x,y: "Ошибка. Деление на 0"if y==0 else x/y

# def add(x,y):
#     return x+y
#
# def subtract(x,y):
#     return x-y
#
# def multiply(x,y):
#     return x*y

# def divide(x,y):
#     if y==0:
#         return "Ошибка. деление на ноль"
#     else:
#         return x/y

print("Выбирите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

# Проверяем на введенное число. Должно быть одно из укзанных в списке
valid_choices = ["1", "2", "3", "4"]
choice = None
while choice not in valid_choices:
    choice = input("Введите номер опереции: ")
    if choice not in valid_choices:
        print("Вы ввели не 1,2,3 или 4.")


nam1 = get_namber("Введите первое число: ")
nam2 = get_namber("Введите второе число: ")

if choice == "1":
    print(f"Результат: {nam1}+{nam2} = {add(nam1,nam2)}")
elif choice == "2":
    print(f"Результат: {nam1}-{nam2} = {subtract(nam1,nam2)}")
elif choice == "3":
    print(f"Результат: {nam1}*{nam2} = {multiply(nam1,nam2)}")
elif choice == "4":
    result = divide(nam1,nam2)
    if isinstance(result,str):
        print(result)
    else:
        print(f"Результат: {nam1}/{nam2} = {result:.2f}") # Оставляет 2 знака после запятой


