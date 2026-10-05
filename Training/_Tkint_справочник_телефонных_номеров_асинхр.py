from tkinter import *
from tkinter import messagebox as mb
from tkinter.messagebox import showerror, showinfo

#Добавить
def add_item():
    if s.get()=='0':
        l1.insert(END, e.get()) # Добавить в список из элемента e
        e.delete(0, END) # Очистить список от 0 до конца
    else:
        if validate_phon():
            l2.insert(END, e.get())  # Добавить в список из элемента e
            e.delete(0, END)  # Очистить список от 0 до конца
#            showerror('Добавление номера','Номер телефона добавлен')

# Удалить
def dell_item():
    if s.get() == '0':
        l1.delete(ANCHOR) # ANCHOR Удалить где стоит курсор
    else:
        l2.delete(ANCHOR)  # ANCHOR Удалить где стоит курсор


#Сохранить
def save():
    try:
        with open('phons.txt', 'w',encoding='utf-8') as f:
            for i in range (l1.size()):
                f.write(f'{l1.get(i)} : {l2.get(i)}\n')
        showinfo('Сохранение','Контакты успешны сохранены')
    except Exception as e:
        showerror(f'Ошибка {e}')


def load():
    try:
        with open('phons.txt','r',encoding='utf-8') as f: # 'r' Открыть фаил для чтения
            l1.delete(0, END) # Перез загрузкой очищаем поле l1 от начала до конца
            l2.delete(0, END)
            for line in f:
                name, _, phone = line.partition(" : ") # Разделить конструкцию списка на 3 части
                l1.insert(END, name)
                l2.insert(END, phone)
        showinfo("Загрузка", "Контакты успешно загружены")
    except FileNotFoundError:
        showerror("Ошибка","Не найден фаил для загрузки телефонных номеров")
    except Exception as e:
        showerror("Ошибка",{e})

def validate_phon(): # Проверка телефонного номера
    namber = e.get() # Получаем телефонный номер из поля ввода e
    if len(namber) == 10 and namber.isdigit() and namber.startswith('9'):
        showinfo('Проверка', 'Номер телефона прошел проверку')
        return True
    else:
        showerror("Ошибка", "Номер должен быть десятизначным, состоять толькоиз цифр и начинатьсяб с '9'.")
        return False



window = Tk()
s= StringVar(value=0)

f1 = Frame()
f1.pack(side=LEFT)
m1= Label(f1, text='Имена')
m1.pack()
l1 = Listbox(f1)
l1.pack()

f2 = Frame()
f2.pack(side=LEFT)
m2= Label(f2, text='Телефоны')
m2.pack()
l2 = Listbox(f2)
l2.pack()

f3 = Frame()
f3.pack(side=RIGHT)

radio1 = Radiobutton(f3, text='Имя', value=0, variable= s)
radio1.pack()
radio2 = Radiobutton(f3, text='Телефон', value=1, variable= s)
radio2.pack()


e= Entry(f3, font='arial 12 bold')# Поле ввода
e.pack() # Поле ввода добавить на форму
b1 = Button(f3, text="Добавить", command=add_item) # Кнопка добавить
b1.pack(pady=5)
b2 = Button(f3, text="Удалить", command=dell_item) # Кнопка Удалить
b2.pack()
b3 = Button(f3, text="Сохранить", command=save) # Кнопка Сохранить
b3.pack(pady=5)
b4 = Button(f3, text="Загрузить", command=load) # Кнопка Сохранить
b4.pack(pady=5)



window.mainloop()

