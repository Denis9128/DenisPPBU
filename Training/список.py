c= list(range(100))
print(c)

Frukt=['Яблоко','Апельсин']
Frukt.append('Банан')
Frukt.append('Картофель')
Frukt.append(100)
f = Frukt[2]
Frukt[1]='Лимон'#Замена 1 элемента
DelFr = Frukt.pop(3) # Удалить 3 элемент

connectList = Frukt + c # Соединить два списка

print(Frukt)
print(f)
print(DelFr)
print(connectList)

Proverka = 'Яблоко'in Frukt
Proverka2 = 'Яблоко' not in Frukt
print(Proverka, Proverka2)

lengthList = len(Frukt) # Количество элементов
print(lengthList)
