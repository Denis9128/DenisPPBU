from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t = 0
music = False

def set():
    global t
    rem = sd.askstring('Время напоминания','Введите время напомнинания в формате ЧЧ:ММ в 24 часовом формате')
    if rem:
        try:
            hour = int(rem.split(':')[0]) # Делим введенные данные по символу ":", т.е делим пополам, берем 0 часть
            minute = int(rem.split(':')[1]) # Получаемминуты, после знака
            now = datetime.datetime.now() # Получаем текущее время
            print(now)
            dt = now.replace(hour=hour, minute=minute, second=0) # Заменяем данные часы и минуты текущие на часы и минуты из ввода
            print(dt)
            t = dt.timestamp() # Переводим полученное время с секунды
            print(t)
            check()

        except Exception as e:
            mb.showerror('Ошибка',f'Произошла ошибка {e}')


def check():
    global t
    if t:
        now = time.time() # Текущее время
        if now >=t:
            play_snd()
            t=0
        window.after(10000, check) # Вызвать функцию через 10000

def play_snd():
    global music
    music =True
    pygame.mixer.init()
    pygame.mixer.music.load('remainder.mp3') #Загрузить указанный фаил с музыкой
    pygame.mixer.music.play() # Запустить файл с музыкой

def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    Label.config(text='Установить новое напоминание')


window = Tk()
window.title("Напоминание")
window.geometry('300x150+900+300')

label = Label(text='Установите напоминание', font=('Arial',14))
label.pack(pady=10)


set_button = Button(text='Установить напоминание', command=set)
set_button.pack(pady=10)

stop_music = Button(text='Остановить музыку', command=stop_music)
stop_music.pack(pady=10)



window.mainloop()