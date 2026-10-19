from tkinter import *
from PIL import ImageTk, Image
from io import BytesIO                    #Библиотека ввода вывода
import requests
from click import command


def load_image(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as er:
        print('Ошибка',er)
        return None

def set_image():
#    url = 'https://cataas.com/cat'
    img = load_image(url)
    if img:
        label.configure(image=img)
        label.image = img

def open_new_window():
    img = load_image(url)
    if img:
        new_window = Toplevel(root) # Новое окно
        new_window.title('Картинка с котиком')
        new_window.geometry('620x520')
        label = Label(new_window, image=img)
        label.image = img
        label.pack()

def command_exit():
    root.destroy()



root = Tk()
root.title('Cats')
root.geometry('620x520')
label = Label(root)
label.pack()

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Фаил', menu=filemenu)
filemenu.add_command(label='Загрузить фото', command=open_new_window)
filemenu.add_separator()
filemenu.add_command(label='Выход', command=command_exit)



update_btn = Button(text='Cледующая', command=set_image)
update_btn.pack(pady=5)

url = 'https://cataas.com/cat'

set_image()

root.mainloop()