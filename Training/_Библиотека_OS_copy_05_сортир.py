"""Копированеи дерева только с картинками"""
from tkinter import *
from tkinter import filedialog as fd
import os
import shutil
from datetime import datetime
from tkinter.messagebox import showinfo


def choose_dir():
    direct = fd.askdirectory()
    if direct:
        organize_photos(direct)

def organize_photos(directory):
    for file in os.listdir(directory): # Перебираем файлы в выбранной категории
        if file.lower().endswith(('.jpg', '.jpeg', '.png')): #Выбираем только те файлы у которых указанное расширение, преобразовываем расширение в нижний регистр lower()
            file_path = os.path.join(directory, file) # путь к файлу в папке directory
            timestamp = os.path.getmtime(file_path)  # Получаем время в секундах
            date = datetime.fromtimestamp(timestamp) # Переводим секунды в дату
            year_month =  date.strftime('%Y_%m') # Оставляем только год и месяц в наименовании
            new_dir = os.path.join(directory, year_month) # Создаём новую директория в названии год и месяц
            if not os.path.exists(new_dir): #Если нет  такой директории, создаем
                os.makedirs(new_dir) # создаем новую директорию если нет
            shutil.move(file_path, os.path.join(new_dir, file)) # отправить фаил в новую директорию

    showinfo('Готово','Все фотографии рассортированы')


window = Tk()
window.withdraw() # Не показывать окно



choose_dir()

window.mainloop()