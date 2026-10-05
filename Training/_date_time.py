from datetime import datetime,date,timedelta,time

d = date(2004,12,31)
t = time(12,31,16)
print(d)
print(t)

dt = datetime.combine(d, t) #Объединяет время
print(dt)

print(d, type(d))
print(t, type(t))
print(dt, type(dt))

d = date.today()
print(d)

dt = datetime.now().replace(microsecond=0) # Убрать микросекунды
print(dt)

dt = datetime.now().replace(year=2020, hour=23) # заменить год или месяц....
print(dt)

# dtt = input('Введите дату(дд.мм.гггг):')
# datt = datetime.strftime(dtt, '%d.%m.%Y')
# print(datt)

print(datetime.strftime(datetime.now(), "%d-%m-%Y %H:%M:%S"))
print(datetime.strftime(datetime.now(), "%A-%m-%B %H:%I:%p"))

dt = datetime.now().replace(microsecond=0)
dttt = dt.timetuple()
for i in dttt:
    print(i)

dtt = dt.isocalendar()
print(dtt)
print(dt.weekday())
print(dt.isoweekday())

days = ('Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье')
print(days[dt.weekday()])







