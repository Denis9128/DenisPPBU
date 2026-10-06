from tkinter import *
from tkinter import  filedialog as fd
from tkinter.messagebox import showerror
import time
from googletrans import Translator, LANGUAGES
from transliterate import translit,get_available_language_codes
from deep_translator import GoogleTranslator



def delete():
    text.delete(1.0, END)
    update_status()

def transliter():
    try:
        sours_text = text.get(1.0, END)
        t_text = translit(sours_text,'ru', reversed=True)
        text.delete(1.0, END)
        text.insert(1.0, t_text)
    except Exception as e:
        showerror('Ошибка',f'Произошла ошибка {e}')
    update_status()

def translate_text():
    try:
        sours_text = text.get(1.0, END).strip()
        translator= GoogleTranslator()

        t_text = translator.translate(sours_text, src='ru', dest='en')
        text.delete(1.0, END)
        text.insert(1.0, t_text)
    except Exception as e:
        showerror('Ошибка', f'Произошла ошибка перевода {e}')
        print(e)
    finally:
        time.sleep(3)



def insert():
    try:
        file = fd.askopenfilename() # Открывает диалоговое окно, для выбора файла
        if file:  # Проверяем, выбран ли файл
            with open(file, 'r', encoding='utf-8') as f:  # encoding='utf-8'
                s = f.read()
            text.insert(1.0, s)
    except FileNotFoundError:
        showerror("Ошибка", "Файл не найден")
    except Exception as e:
        showerror("Ошибка", f"Произошла ошибка: {e}")
    update_status()


def save():
    try:
        file = fd.asksaveasfilename( #asksaveasfilename - окно диалога сохранения файла
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        if file:  # Проверяем, выбран ли файл
            with open(file, 'w') as f:
                s = text.get(1.0, END) # Извлекаем текст введенный ползователем в реквизите
                f.write(s)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Не удалось сохранить файл")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


def quit():
    window.destroy() # Закрыть окно

def update_status():
    content = text.get(1.0, END) # Получить с 1 до последнего символа
    char_content = len(content)
    word_count = len(content.split())
    status_label.config(text=f'Символов: {char_content} Слов {word_count}')



window = Tk()
window.title('Photo')

frame = Frame(window)
frame.pack()

# window.geometry('500x500')
mainmenu_bar = Menu(window)
window.config(menu=mainmenu_bar)

file_menu = Menu(mainmenu_bar, tearoff=0) # tearoff=0 - Отключение пунктирной линии

mainmenu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label='Открыть', command=insert)
file_menu.add_command(label='Сохранить', command=save)
file_menu.add_command(label = 'Удалить', command=delete)

#file_menu.add_command(label='Открыть...', command=open)
file_menu.add_separator() # Добавление линии разделителя между пунктами меню
file_menu.add_command(label="Выход", command=quit)

process_menu = Menu(mainmenu_bar, tearoff=0)
mainmenu_bar.add_cascade(label='Обработка', menu=process_menu)
process_menu.add_command(label='Транслитерация', command=transliter)
process_menu.add_command(label='Перевод на английский', command=translate_text)


text = Text(frame, width=30, height=8, bg="light gray", wrap=WORD) # Вставка текстового поля на форму wrap=WORD - перенос текста по словам
text.pack(side=LEFT)
text.bind('<Key>', lambda event:update_status()) # При каждом клике вызывается функция

scroll = Scrollbar(frame, command=text.yview) # Прокрутка command=text.yview - прокрутка по вертикали
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set) # Прокрутка Scrollbar вместе с текстом

status_label = Label(text='proba', anchor=W)
status_label.pack(fill=X)


update_status()
window.mainloop()
