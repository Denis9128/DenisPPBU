from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo, showerror

from PIL import Image
import stepic

def open_file():
    file = askopenfilename(filetypes=[('Image','*.jpg *.png *.bmp *.jpeg')])
    file_path.set(file)

def encod_text():
    image_path = file_path.get()
    text = text_to_encod.get()
    output_path = 'encoded.png'

    try:
        image = Image.open(image_path)
        encod_image = stepic.encode(image, text.encode())
        encod_image.save(output_path)
        showinfo('Успешно','Текст зашифрован')
    except Exception as e:
        showerror('Ошибка',f'Ошибка {e}')

def decod_text():
    image_path = file_path.get()
    try:
        image = Image.open(image_path)
        decoded_text = stepic.decode(image)
        showinfo('Декодированный текст',decoded_text)
    except Exception as e:
        showerror('Ошибка',f'Ошибка {e}')




window = Tk()
window.title('Стеганография')

file_path = StringVar()

Label(text='Путь к изображению').pack()
Entry(textvariable=file_path, width=60).pack(padx=10)
Button(text='Выбрать фаил', command=open_file).pack(pady=5)

text_to_encod = StringVar()
Label(text='Текст для шифрования').pack(padx=10)
Entry(textvariable=text_to_encod, width=60).pack()

Button(text='Зашифровать текст', command=encod_text).pack(pady=5)
Button(text='Расшифровать текст текст', command=decod_text).pack(pady=5)

window.mainloop()

