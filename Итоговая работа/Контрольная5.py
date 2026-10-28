from tkinter import *
from tkinter import messagebox as mb
from tkinter.messagebox import showinfo
from tkinter import ttk
from datetime import *
import requests


def update_currency_label(event):
    code = target_combobox.get().strip()
    name = correncies[code]
    target_label.config(text = name)


def update_base_label(event):
    base_label.config(text='')
    code = base_combobox.get().strip()
    name = correncies[code]
    base_label.config(text = name)


def update_second_base_label(event):
    second_base_label.config(text='')
    code = second_base_combobox.get().strip()
    name = correncies[code]
    second_base_label.config(text = name)


def exchange():

    global currency_list_info

    currency_list = [] # Список валюты
    #

    base_cod = base_combobox.get() #Базовая валюта
    currency_list.insert(0,base_cod)

    second_base_cod = second_base_combobox.get()  # Вторая базовая валюта
    currency_list.insert(1,second_base_cod)

    target_cod = target_combobox.get()  # Целевая валюта

    for cod in currency_list:

        if target_cod and cod:
            try:
                response = requests.get(f'https://open.er-api.com/v6/latest/{cod}')
                response.raise_for_status()
                data = response.json()
                if target_cod in data['rates']:
                    exchange_rate = data['rates'][target_cod]
                    base = correncies[cod]
                    target = correncies[target_cod]

                    currency_info = (f'{exchange_rate:.2f} {target} за 1 {base}.')
                    currency_list_info.insert(0, currency_info)

                else:
                    mb.showinfo('Ошибка!', f'Валюта {target_cod} не найдена.')
            except Exception as e:
                mb.showinfo('Ошибка!', f'{e}')
        else:
            currency_list_info = [] # Если не выбран код, очищаем ранее сформированный список
            showinfo('Внимание!','Выберите код валюты.')
    if currency_list_info:
        form_the_final_list()


def form_the_final_list():
    global currency_list_info


    current_time = datetime.today()  # Текущее время
    ru = ""
    m = current_time.month  # Получаем номер месяца
    if m == 1:
        ru = "Янвря"
    elif m == 2:
        ru = "Февряля"
    elif m == 3:
        ru = "Марта"
    elif m == 4:
        ru = "Апреля"
    elif m == 5:
        ru = "Мая"
    elif m == 6:
        ru = "Июня"
    elif m == 7:
        ru = "Июля"
    elif m == 8:
        ru = "Августа"
    elif m == 9:
        ru = "Сентября"
    elif m == 10:
        ru = "Октября"
    elif m == 11:
        ru = "Ноября"
    elif m == 12:
        ru = "Деабря"

    time_tek = current_time.strftime(f"%d {ru} %Y")

    currency_window = Toplevel(root)
    currency_window.title(f'Курс обмена валюты на {time_tek}')
    currency_window.geometry('500x50+700+350')
    if currency_list_info:
        info = f'{currency_list_info[1]}\n{currency_list_info[0]}'

        label = Label(currency_window, text=info, justify='left')
        label.pack()
    else:
        showinfo('Внимание!', 'Выберите код валюты.')

correncies = {'EUR':'Евро',
              'USD':'Доллар США',
              'RUB': 'Российский рубль',
              'JPY':'Японская йена',
              'GBP':'Фунт стерлингов',
              'AUD':'Австралийский доллар',
              'CHF':'Швейцарский франк',
              'CAD': 'Канадский доллар',
              'CNY': 'Китайский юань',
              'KZT': 'Казахстанский тенге',
              'UZS': 'Узбекский сум'
              }


currency_list_info = [] # Список курсов


root = Tk()
WIDTH = root.winfo_screenwidth() # Размер ширины экрана монитора
HEIGHT = root.winfo_screenheight()  #Размер высоты экрана монитора
root.title('Курсы обмена валюты')
x  = 360
y = 260
root.geometry(f'{x}x{y}+{WIDTH // 2 - x // 2}+{HEIGHT // 2 - y // 2 - 25}')

Label(root, text= 'Базовая валюта',font=('Arial',12)).pack()
base_combobox = ttk.Combobox(root, values=list(correncies.keys()))
base_combobox.pack(pady=3, padx=3)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)

base_label = ttk.Label()
base_label.pack()

Label(root, text= 'Вторая базовая валюта',font=('Arial',12)).pack()
second_base_combobox = ttk.Combobox(root, values=list(correncies.keys()))
second_base_combobox.pack(pady=3, padx=3)
second_base_combobox.bind('<<ComboboxSelected>>', update_second_base_label)

second_base_label = ttk.Label()
second_base_label.pack()

Label(root, text='Целевая валюта',font=('Arial',12)).pack()

target_combobox = ttk.Combobox(root, values=list(correncies.keys()))  #Целевая валюта
target_combobox.pack(pady=3, padx=3)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

target_label = ttk.Label()
target_label.pack()

Button(text='Получить курс обмена валют', command=exchange).pack(pady=10, padx=10)

root.mainloop()