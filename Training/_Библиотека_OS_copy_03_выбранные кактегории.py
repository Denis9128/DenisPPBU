"""Копированеи дерева только с картинками"""
from tkinter import *
from tkinter import filedialog as fd
import os
import shutil

window = Tk()
window.withdraw() # Не показывать окно

direct = fd.askdirectory(title='Выбирите папку с изображениями для их копирования')
if direct:
    new_dir = direct + '_new'
    if not os.path.exists(new_dir): # Если не существует папка new_dir, создаем
       os.makedirs(new_dir) # Создаём папку
    else:
        print(f'Папка {new_dir}, уже существует.')
    for file in os.listdir(direct): # Перебираем файлы в выбранной директории
        if file.lower().endswith(('.jpg', '.jpeg', '.png')): # Отбираем по расширению.
            sourse_file = os.path.join(direct, file) # Источник
            distination_file = os.path.join(new_dir, file) # путь назначения

            try:
                shutil.move(sourse_file, distination_file) # копируем из источника в папку назначения
                print('Фаил перемещен')
            except Exception as e:
                print(f'Ошибка перемещения файла {file}: {e}')

    print('Всё скопировано')
else:
    print('Папка не была выбрана')


window.mainloop()