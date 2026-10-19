"""Копированеи дерева"""
from tkinter import *
from tkinter import filedialog as fd
import os
import shutil

window = Tk()
window.withdraw() # Не показывать окно

direct = fd.askdirectory(title='Выбирите папку для копирования')
if direct:
    new_dir = direct + '_new'
    if not os.path.exists(new_dir): # Если не существует папка new_dir, создаем
        try:
            shutil.copytree(direct, new_dir) # копирование папка direct в new_dir
            print(f'Всё содержимое папки {direct}, скопировано в папку {new_dir} ')
        except Exception as e:
            print(f'При копировании ошибка:{e}')
    else:
        print(f'Папка {new_dir}, уже существует.')
else:
    print('Папка не была выбрана')


window.mainloop()