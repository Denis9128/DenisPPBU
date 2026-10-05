import datetime

segodnia = datetime.datetime.today()
taim = segodnia.strftime('%H:%M:%S')
# ru = ""
m = segodnia.month # Получаем номер месяца
spisokmes = ["Января","Февраля","марта","Апреля","Мая",
             "Июня","Июля","Августа","Сентября","Октября",
             "Ноября","Декабря"]
monht_Ru =spisokmes[m - 1]

print(f'Сегодня: {segodnia.day} {monht_Ru} {segodnia.year}, {taim}')