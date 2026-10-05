import datetime

segodnia = datetime.datetime.today()
taim = segodnia.strftime('%H:%M:%S')
ru = ""
m = segodnia.month # Получаем номер месяца
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

print(f'Сегодня: {segodnia.day} {ru} {segodnia.year}, {taim}')