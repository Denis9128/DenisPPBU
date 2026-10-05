"""Словари dict
Неупорядоченный набор пар Ключ: значение,
в которых ключ уникален"""

d = {}
d= {'Pb':'Свинец',
    'Au':'Золото'}
print(d)

print(d['Au'])
print(d.get('Pb', 'не найдено')) # Исключает ошибки при вводе
d['Pb'] = 'свинец' #Меняет данные в ключе
print(d.get('Pb', 'не найдено'))
d['Fe'] = 'Железо'
print(d)
d.setdefault('Fe', 1000) # запрещает присвоение значение 1000 указанному ключу если найден ключ
print(d)

d.setdefault(1, 1000) # если ключ не найден то добавляет новую запись в библиотеку
print(d)

d.update({3:33, 1:11}) # Обновляет данные в словаре в данном случае ключ 1, поменял значение на 11
print(d)

n = d.pop('Pb') # удаляет ключ и значение
print(n)
print(d)

n= d.pop('Au')
nn = d.popitem() #Удалить последние доьбавленные значения
print(nn)
print(d)

print(d.keys()) # вывод ключей
print(d.values()) # Вывод значений
print(d.items()) #

for i in d:
    print(i)

list = [('Pb1','Свинец1'),('Pb2','Свинец2'),(11,111)]
dd =dict(list)
print(dd)

list = [11,22,33]
dd =dict.fromkeys(list,100)
print(dd)

dd = {i: i**2 for i in range(10,20)}
print(dd)




