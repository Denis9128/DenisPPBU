from tkinter import *

def draw_circle(): #
    color = color_var.get()
    canvas.create_oval(50,50,150,150, outline='red', fill=color)

def draw_triangle():
    color = color_var.get()
    canvas.create_polygon(50,150,100,50,150,150, outline='red', fill=color)

def draw_square():
    color = color_var.get()
    canvas.create_rectangle(50,50,150,150, outline='red', fill=color)

def cltare_canvas():
    canvas.delete('all')


window = Tk()
window.title("Рисование фигур")
window.geometry('400x600')

color_var = StringVar(value='blue')

canvas = Canvas(window, width=300, height=200)
canvas.pack(pady=10)

circle_batton = Button(text='Окружность', command=draw_circle)
circle_batton.pack(pady=10)

triangle_batton = Button(text='Треугольник', command=draw_triangle)
triangle_batton.pack(pady=10)

square_button = Button(text='Квадрат', command=draw_square)
square_button.pack(pady=10)

clear_batton = Button(text='Очистить', command=cltare_canvas)
clear_batton.pack(pady=10)


blue_radio = Radiobutton(text='Синий', variable=color_var, value='blue')
blue_radio.pack()

Red_radio = Radiobutton(text='Красный', variable=color_var, value='red')
Red_radio.pack()

black_radio = Radiobutton(text='Черный', variable=color_var, value='black')
black_radio .pack()


window.mainloop()
