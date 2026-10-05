contacts = {}
def input_contact():
    name = input("Введите имя: ")
    phon = input("Введите десятизначный номер телефона +7")
    if len(phon) ==10 and phon.isdigit() and phon.startswith("9"): # Проверка 10 символов и телефон должен быть цифры начинаться с 9
        contacts[name] = phon
        print("Контакт добавлен")
        print(contacts)
    else:
        print("Не верный номер телефона")

def find_contact(): # Поиск контакта
    name = input("Введите имя для поиска: ")
    print(contacts.get(name,"Контакт не найден")) # Поиск контакта
    # if name in contacts:
    #     print(contacts[name])
    # else:
    #     print("Контакт не найден!")

def delete_contact(): #Удаление контакта
    name = input("Введите имя для удаления: ")
    try:
        del contacts[name]
        print(contacts)
    except KeyError:
        print('Контакт не найден')


while True:
    action = input("Выберите действие: Добавить 1, Найти 2, Удалить 3, Выйти 4: \n:")
    if action == "1":
        input_contact()
    elif action == "2":
        find_contact()
    elif action == "3":
        delete_contact()
    elif action == "4":
        break
    else:
        print("Неверный ввод.")


