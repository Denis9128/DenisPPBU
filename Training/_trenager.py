from tkinter import *
import time
from tkinter import messagebox
from tkinter.messagebox import showinfo, askyesno, showerror


def load_phraze():
    try:
        with open('phraze.txt') as f:
            return f.read().strip()
    except FileNotFoundError:
        showerror('Ошибка','Фаил с фразой не найден')
        return 'quickbrownfox'

def start():
    global i,t
    i = 0
    t = time.time() # текущее время
    label.config(text=phraze[i]) # выводим первый символ
    window.bind('<Key>', check)


def check(event):
    global i
    if event.char == phraze[i]: # event.char - введенный симфол с клавиатуры
        i+=1
        if i==len(phraze):
            finish()
        else:
            label.config(text=phraze[i])
    else:
        label.config(text=f'Ошибка! ожидалась буква {phraze[i]}, \nнажмите любую клавишу для продолжения.',font=('helvetica', 15))
        window.bind('<Key>', cont)


def finish():
    elapsed = time.time() - t # текущее время - время начала (Считаем время от начала до окончания)
    time_allowed = len(phraze)
    if elapsed <= time_allowed: # если затраченое время  меньше или равно количеству символов в фразе
        rez = f'Вы победили! Ваше время {elapsed:.1f} сек. Время для прохожденя {time_allowed} секунд'
        window.unbind('<Key>') # .unbind() отвязываем все текущие обработчики ввода
    else:
        rez = f'Прошло {elapsed:.1f} сек. \nВы проиграли! Время для прохожденя {time_allowed} секунд'
        window.unbind('<Key>')
    showinfo('Результат',rez)
    if askyesno('Повторить?','Хотите попробовоть еще раз?'): # Вопрос продолжить или нет если да, то start()
        start()
    else:
        window.destroy() # Уничтожить окно если нет

def cont(event):
    global i
    label.config(text=phraze[i], font=('Helvetica', 25))
    window.bind('<Key>', check)



i = 0
t = 0
phraze = load_phraze()

window = Tk()
window.title('Клавиатурный тренажер')
window.geometry('500x100')

label = Label(font=('Helvetica', 25))
label.pack()


start()
window.mainloop()