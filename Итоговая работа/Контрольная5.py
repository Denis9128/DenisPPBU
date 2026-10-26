from tkinter import *
from tkinter import messagebox as mb
from tkinter.messagebox import showinfo
from tkinter import ttk
from datetime import *
import requests

import json
import pprint

from zmq.backend import second

name_val = ''

def update_currency_label(event):
    # update_currency_label.config(text='')
    code = target_combobox.get().strip()
    name = correncies[code]
    target_label.config(text = name)
    global name_val
    name_val = name

def update_base_label(event):
    base_label.config(text='')
    code = base_combobox.get().strip()
    name = correncies[code]
    base_label.config(text = name)
    # global name_val
    # name_val = name

def Second_update_base_label(event):
    second_base_label.config(text='')
    code = second_base_combobox.get().strip()
    name = correncies[code]
    second_base_label.config(text = name)
    # global name_val
    # name_val = name

def exchange():
    currency_list = []

    base_cod=base_combobox.get() #Базовая валюта
    currency_list.insert(0,base_cod)

    # base_cod = base_combobox.get()  # Базовая валюта

    second_base_cod = second_base_combobox.get()  # Вторая базовая валюта
    currency_list.insert(1,second_base_cod)
    # print(currency_list)

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
                    # currency_name = correncies[code]
                    now = datetime.now()
                    current_time = now.today()
                    time_tek = current_time.strftime("%H:%M")

                    mb.showinfo('Курс обмена', f'Курс валюты на {time_tek} :\n{exchange_rate:.1f} {target} за 1 {base}')


                else:
                    mb.showinfo('Ошибка', f'Валюта {target_cod} не найдена.')
            except Exception as e:
                mb.showinfo('Ошибка', f'{e}')
        else:
            showinfo('Внимание','Выберите код валюты.')

correncies = {'EUR':'Евро',
              'USD':'Доллар США',
              'RUB': 'Российский рубль',
              'JPY':'Японская йена',
              'GBP':'Фунт стерлингов',
              'AUD':'Австралийский доллар',
              'CHF':'Швейцарский франк',
              'AUD': 'Австралийский доллар',
              'CAD': 'Канадский доллар',
              'CNY': 'Китайский юань',
              'KZT': 'Казахстанский тенге',
              'UZS': 'Узбекский сум'
              }

root = Tk()
root.title('Курсы обмена валюты к USD')
root.geometry('360x260')

Label(root, text= 'Базовая валюта',font=('Arial',12)).pack()
base_combobox = ttk.Combobox(root, values=list(correncies.keys()))
base_combobox.pack(pady=3, padx=3)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)

base_label = ttk.Label()
base_label.pack()

Label(root, text= 'Вторая базовая валюта',font=('Arial',12)).pack()
second_base_combobox = ttk.Combobox(root, values=list(correncies.keys()))
second_base_combobox.pack(pady=3, padx=3)
second_base_combobox.bind('<<ComboboxSelected>>', Second_update_base_label)

second_base_label = ttk.Label()
second_base_label.pack()

Label(root, text='Целевая валюта',font=('Arial',12)).pack()

# popular_currencies = ['EUR', 'USD', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'RUB','KZT', 'UZS']

target_combobox = ttk.Combobox(root, values=list(correncies.keys()))  #Целевая валюта
target_combobox.pack(pady=3, padx=3)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

target_label = ttk.Label()
target_label.pack()

Button(text='Получить курс обмена к доллару', command=exchange).pack(pady=10, padx=10)


# p = pprint.PrettyPrinter(indent=4)
# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
#
# p.pprint(data)


root.mainloop()