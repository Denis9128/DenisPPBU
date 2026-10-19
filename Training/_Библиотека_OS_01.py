''''Программа для вывода всех файлов в выбранной директории'''''
import os
from tkinter import *
from tkinter import filedialog as fd
from datetime import datetime


window = Tk()
window.withdraw() # Не выводить окно

direct = fd.askdirectory() # выбрать фаил
if direct:
    for file in os.listdir(direct): # Список всех файлов в директории
        if file.lower().endswith((".jpg",".jpeg",".png",".bmp")): # Выбираем файлы только нужного расширения
            file_path = os.path.join(direct, file) # Путь к файлу
            lt = os.path.getatime(file_path) # Получае дату файла в секундах
            ft = datetime.fromtimestamp(lt).strftime('%Y-%m-%d %H:%M:%S') # Перефодим из секунд в дату по шаблону strftime

            print(file, ft)

window.mainloop()