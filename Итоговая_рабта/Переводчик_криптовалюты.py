from tkinter import *
from tkinter import messagebox as mb
from tkinter.messagebox import showinfo
from tkinter import ttk
from datetime import *
import requests
from transliterate.contrib.languages import bg


def update_currency_label(event): # Обновляет label с наименованием валюты
    currency_label.config(text='') # Очищаем если что то было написано
    code = combobox.get() # Получаем данные из комбобокса
    name = correncies[code]
    currency_label.config(text = name.capitalize())


# data = requests.get("https://api.coinlore.net/api/tickers/",
#                  params={"start": 0, "limit": 100})
#
#
#
# for coin in data.json()["data"]:
#     print(coin["symbol"], coin["price_usd"])


def exchange():
    code = combobox.get().upper()
    if code:
        try:
            currency_name = correncies[code]
            if source_var.get() == 'https://api.coingecko.com':
                response = requests.get((f'https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids={currency_name}&x_cg_demo_api_key=CG-yHwb17uNimkYBcHgH7QneHVE'),timeout=10)

                data = response.json()
                if currency_name.lower() in data:
                    price = data[currency_name.lower()].get('usd')
                    currency_label.config(text = (f'За 1 {(currency_name).capitalize()}, {price:.2f} $ США'), foreground='#85bb65', font=('Arial', 15))

            if source_var.get() == 'https://api.coinlore.net':
                response2 = requests.get("https://api.coinlore.net/api/tickers/",timeout=10, params={"start": 0, "limit": 100})
                data2 = response2.json()["data"]

                for coin in data2:
                    if coin.get('symbol') == code:
                        price = float(coin.get('price_usd')) # Переводим строку в число с плавающей точкой
                        currency_label.config(text=(f'За 1 {(currency_name).capitalize()}, {price:.2f} $ США'),
                                              foreground='#85bb65', font=('Arial', 15))

        except Exception as e:
            showinfo('Ошибка', f'Ошибка при получении цены {e}')
    else:
        showinfo('Внимание','Выберите код валюты.')


# Словарь популярной криптовалюты
correncies = {'BTC':'Bitcoin',
              'ETH':'Ethereum',
              'USDT': 'tether',
              'BNB': 'binancecoin',
              'SOL': 'solana',
              'USDC': 'usd-coin',
              'XRP': 'ripple',
              'ADA': 'cardano',
              'DOGE': 'dogecoin',
              'DOT': 'polkadot',
              'SHIB': 'shiba-inu',
              'WBTC': 'wrapped-bitcoin',
              'AVAX': 'avalanche-2',
              'LINK': 'chainlink',
              'BCH': 'bitcoin-cash',
              'LTC': 'litecoin',
              'UNI': 'uniswap',
              'ICP': 'internet-computer',
              'XLM': 'stellar',
              'ETC': 'ethereum-classic',
              'DAI': 'dai',
              'APE': 'ape',
              'ATOM': 'cosmos',
              'XTZ': 'tezos',
              'ALGO': 'algorand',
              'VET': 'vechain',
              'EOS': 'eos'}


root = Tk()
root.configure(background='white')
root.title('Курсы обмена криптовалюты к USD')
WIDTH = root.winfo_screenwidth() # Размер ширины экрана монитора
HEIGHT = root.winfo_screenheight()  #Размер высоты экрана монитора
x  = 400
y = 200
root.geometry(f'{x}x{y}+{WIDTH // 2 - x // 2}+{HEIGHT // 2 - y // 2 - 25}') # окно root в центре экрана



frame = Frame(root,background='white')
frame.pack()

Label(frame, text = 'Выберите источник:',background='white').grid(row=0, column=0, pady= 5,sticky='w')

source_var = StringVar(value='https://api.coingecko.com')

radbatt1 = Radiobutton(frame, text='api.coingecko.com',background='white',variable=source_var, value='https://api.coingecko.com')
radbatt1.grid(row=0, column=1,sticky='w')

radbatt2 = Radiobutton(frame, text='api.coinlore.net',background='white',variable=source_var, value='https://api.coinlore.net')
radbatt2.grid(row=1, column=1,sticky='w')

label = Label(frame, text='Выберите код криптовалюты:      ',background='white')
label.grid(row=2, column=0, pady=5,sticky='w')

combobox = ttk.Combobox(frame, values=list(correncies.keys()),background='white',state="readonly") # Поле только для выбора
combobox.grid(row=2, column=1, pady= 5)
combobox.bind('<<ComboboxSelected>>', update_currency_label)

currency_label = ttk.Label(foreground='#85bb65', font=('Arial', 15),background='white') # label для отображения выбранной валюты
currency_label.pack(pady=5)

Button(text='Получить курс обмена', command=exchange,background='#85bb65').pack(pady=10, padx=10)

root.mainloop()