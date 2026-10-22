from tkinter import *
from tkinter import messagebox as mb
from tkinter.messagebox import showinfo
from tkinter import ttk
from datetime import *
import requests

import json
import pprint

name_val = ''

def update_currency_label(event):
    currency_label.config(text='')
    code = combobox.get()
    name = correncies[code]
    currency_label.config(text = name)
    global name_val
    name_val = name

def exchange():
    code = combobox.get().upper()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                currency_name = correncies[code]
                now = datetime.now()
                current_time = now.today()
                time_tek = current_time.strftime("%H:%M:%S")
                mb.showinfo('Курс обмена',f'Курс валюты {name_val} на {time_tek} к USD:\n {exchange_rate} {code} за 1 USD')
            else:
                mb.showinfo('Ошибка', f'Валюта не найдена.')
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
              'CHF':'Швейцарский франк',}


root = Tk()
root.title('Курсы обмена валюты к USD')
root.geometry('360x180')

Label(root, text='Введите код валюты').pack(padx=10, pady=10)
popular_currencies = ['EUR', 'USD', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'RUB','KZT', 'UZS']

combobox = ttk.Combobox(root, values=popular_currencies, state='readonly')
combobox.pack(pady=10, padx=10)
combobox.bind('<<ComboboxSelected>>', update_currency_label)

currency_label = ttk.Label()
currency_label.pack()


# entry = Entry(root)
# entry.pack()

Button(text='Получить курс обмена к доллару', command=exchange).pack(pady=10, padx=10)


# p = pprint.PrettyPrinter(indent=4)
# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
#
# p.pprint(data)


root.mainloop()