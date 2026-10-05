try:
    with open("proba.txt",'w',encoding="utf-8") as file:
        file.write("Новый текст!!!")

except IOError:
    print('Ошибка ввода вывода')
except OSError:
    print("Ошибка операционной системы")
except UnicodeDecodeError:
    print('Ошибка кодирования текста')
except Exception as e:
    print(f'Неизвестная ошибка: {e}')