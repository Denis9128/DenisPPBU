from tkinter import *
from tkinter.messagebox import showerror, showinfo
from PIL import Image, ImageTk, ImageGrab
from tkinter import filedialog

pen_color = 'black' # Цвет линии по умолчанию
thick = 5 # Толщина линии по умолчанию

def draw(event):
    x,y = event.x,event.y # Получаем координаты движения мышкой
    canvas.create_oval(x,y,x+thick,y+thick,fill=pen_color,outline=pen_color)


def change_in_thickness():
    global thick
    try:
        thick = int(thickness.get())
    except ValueError:
        showerror('Ошибка','Толщина линии должна быть написана цифрой, число целое!')


def load_image():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Image file","*.png; *.jpeg; *bmp; *gif")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((600,400))
            image_tk = ImageTk.PhotoImage(image) # преобразовать изображение
            canvas.create_image(0,0,image=image_tk,anchor=NW) # вывести изображение на холст
            canvas.image = image_tk
    except Exception as e:
        showerror('Ошибка',f'Не удалось загрузить фаил {e}')

def save_image():
    try:
        file_pass = filedialog.asksaveasfilename(defaultextension='.png',filetypes=[("Image file","*.png")])
        if file_pass:
            x=window.winfo_rootx()
            y=window.winfo_rooty()
            x1=x+600
            y1=y+400
            ImageGrab.grab().crop((x,y,x1,y1)).save(file_pass)
            showinfo('Сохранено','Изображение сохранено!')
    except Exception as e:
        showerror('Ошибка',f'Ошибка сохранения {e}')
        print({e})

def quit_win():
    window.destroy()

def clear_image():
    canvas.delete('all')



window = Tk()
window.title("Графический редактор")

# Добавляем реквизиты на форму
canvas = Canvas(width=600, height=400, bg='white') # Добавляем полотно
canvas.pack()
canvas.bind('<B1-Motion>', draw)

frame = Frame(window)
frame.pack()

label_line = Label(frame,text='Толщина линии: ') # Надпись Толщина линии
label_line.grid(row=0,column=0)
thickness = Entry(frame, width=5) # Поле ввода толщины линии
thickness.grid(row=0,column=1)
btm = Button(frame, text='Установить толщину', command = change_in_thickness)
btm.grid(row=0, column=2, padx=5)
btm = Button(frame, text='Стереть всё', command = clear_image)
btm.grid(row=0, column=3, padx=5)

colors= ['red','green','blue','black','yellow', 'violet', 'light gray','pink','light green']
for color in colors:
    lbl = Label(bg=color, width=8, height=2)
    lbl.pack(padx=2, pady=5, side = LEFT)
    lbl.bind('<B1-Motion>', lambda e, c=color: globals().update(pen_color=c)) # Клик левой кнопкой


# Добавляем меню
menu_bar =Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Фаил', menu=file_menu)
file_menu.add_command(label='Загрузить изображение', command=load_image)
file_menu.add_command(label='Сохранить изображение', command=save_image)
file_menu.add_separator()
file_menu.add_command(label='Очистить изображение', command=clear_image)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=quit_win)

window.mainloop()