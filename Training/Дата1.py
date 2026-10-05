import datetime
t = datetime.datetime.now()
print(f'Текущее время: {t}')

segodnia = datetime.datetime.today()
date = segodnia.strftime('%d %B %Y')
print(f'Сегодня время: {date}')