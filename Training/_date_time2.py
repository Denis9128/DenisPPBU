from datetime import datetime,date,timedelta,time

berthday = input('Введите дату рождения (дд.мм.гггг): ')
berthday = datetime.strptime(berthday, '%d.%m.%Y').date()
print(berthday)
dt_now = datetime.today()
year = dt_now.year
berthday = berthday.replace(year=year)
#print(berthday,dt_now,year)
if berthday < dt_now:
    berthday = berthday.replace(year=year+1)
rez = berthday - dt_now
print(f'До вашего дня рождения {rez.days}дн')
