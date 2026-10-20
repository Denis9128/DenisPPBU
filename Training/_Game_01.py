from tkinter import *
import random
from tkinter.messagebox import showinfo, askyesno
import time


def move_ball(event):
    key = event.keysym # в функцию-обработчик передаётся объект события нажатия клавиши (стрелок, функциональных клавиш)
    x1,y1, x2,y2 = canvas.coords(ball) # передаем текущие координаты ball
 #   print(x1,y1,x2,y2)
    if key == 'Up' and y1>0: # Если нажата клавиша Up
        canvas.move(ball,0,-20)
    elif key == 'Down' and y2<300:
        canvas.move(ball,0,20)
    elif key == 'Left' and x1 >0:
        canvas.move(ball, -20, 0)
    elif key == 'Right' and x2 < 400:
            canvas.move(ball, 20, 0)
    check_collision()


def check_collision():
    b = canvas.coords(ball)
    # print(b)
    s = canvas.coords(square)
    # print(s)
    if b[2] > s[0] and b[0] < s[2] and b[3]> s[1] and b[1] < s[3]:

        move_square()
        update_score()

def move_square():
    x1,y1 = random.randint(0,300), random.randint(0,280)
    x2,y2 = x1+20, y1+20
    canvas.coords(square,x1,y1,x2,y2)

def update_score():
    global score, start_time
    score += 1
    score_label.config(text=f'Счет: {score}')
    if score >= 10:
        end_time = time.time()
        if end_time - start_time < 20: # Дата начала и дата окончания меньше
            showinfo("Игра окончена",f'Вы набрали {score} очков\nза {(end_time - start_time): .1f} секунд')
        else:
            showinfo('Вы не проиграли',f'Время вышло! Касаний всего{score}')
        if askyesno('Игра окончена','Хотите сыграть еще раз?'):
            start_game()
        else:
            window.destroy()

def start_game():
    global score, start_time
    score = 0
    score_label.config(text=f'Счет: {score}')
    start_time = time.time()  # Время начала игры




window = Tk()
window.title("Игра с шариком")
window.geometry("400x330+1000+400")

canvas = Canvas(width=400, height=300)
canvas.pack()

score = 0
start_time = time.time() # Время начала игры

ball = canvas.create_oval(180,180,220,220,fill="red")         # шар
square = canvas.create_rectangle(150,150,170,170,fill="blue") # Квадрат
score_label = Label(text=f'Счет: {score}')
score_label.pack()

window.bind('<KeyPress>', move_ball)
window.focus_set()

window.mainloop()