import tkinter
from tkinter import *
from tkinter import messagebox as mb
import time
import pygame as pg

pg.mixer.init()
pg.mixer.music.load('music.mp3')


def tick():
    global time_alarm
    current_time = time.strftime("%H:%M:%S")
    if (time_alarm == current_time or
        time_alarm == time.strftime('%H:%M') or
        time_alarm == time.strftime('%H')):
        time_alarm = ''
        pg.mixer.music.play()

    screen_time.after(1000, tick) # вызывает функцию каждую секунду
    screen_time.config(text=current_time)

def on_clik():
    global time_alarm
    time_alarm = entry_time.get().strip()

    mb.showinfo('Включение будильника',
                f'Будильник включен на {time_alarm}')

def off_clik():
    global time_alarm
    time_alarm = ' '
    entry_time.delete(0, END)
    pg.mixer.music.stop()
    mb.showwarning('Выключение будильника',f'Будильник выключен')



time_alarm = ''

root = Tk()
root.title('Будильник')
root.config(background='black')
WIDTH = root.winfo_screenwidth() # Размер ширины экрана
HEIGHT = root.winfo_screenheight()  #Размер высоты экрана
X = 500 #Размер окна программы
Y = 250 #Размер окна программы

# определение геометрии окна программы
root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
              f"+{HEIGHT // 2 - Y // 2 - 25}")

# отбражение текста
screen_time = Label(root, text='00:00:00', font=("Arial", 80))
screen_time.config(bg="black", fg="lime")
screen_time.pack()

#Поле ввода текста
entry_time = Entry(root, width=10, font="Arial 20",justify="center",bg="grey")
entry_time.pack(pady=2)

# Кнопки
on = Button(root, text='Включить', font=("Arial", 10),bg="grey", command=on_clik)
on.pack(pady=5, side=LEFT, padx=50,anchor='center') # отступ от предыдущего элемента
off = Button(root, text='Выключить', font=("Arial", 10),bg="grey",command=off_clik)
off.pack(side=RIGHT, padx=50, anchor='center')

tick()
root.mainloop()