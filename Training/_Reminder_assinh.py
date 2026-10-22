from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


def set():
    rem = sd.askstring('Время напоминания','Введите время напомнинания в формате ЧЧ:ММ в 24 часовом формате')
    if rem:
        try:
            hour = int(rem.split(':')[0]) # Делим введенные данные по символу ":", т.е делим пополам, берем 0 часть
            minute = int(rem.split(':')[1]) # Получаемминуты, после знака
            now = datetime.datetime.now() # Получаем текущее время
            print(now)
            dt = now.replace(hour=hour, minute=minute) # Заменяем данные часы и минуты текущие на часы и минуты из ввода
            print(dt)
            t = dt.timestamp() # Переводим полученное время с секунды
            print(t)



        except Exception as e:
            mb.showerror('Ошибка',f'Произошла ошибка {e}')





window = Tk()
window.title("Напоминание")

label = Label(text='Установите напоминание')
label.pack(pady=10)

set_button = Button(text='Установить напоминание', command=set)
set_button.pack(pady=10)



window.mainloop()