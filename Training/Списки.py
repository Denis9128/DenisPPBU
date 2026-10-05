"""List"""
"""Список - упорядоченный набор объектов"""
nam = [22, 33, 44, 55, 99]
# print(nam[0])
# print(nam[1:-2])
# print(nam[::2]) # Шаг 2
# print(nam[2:])# От 2 до последнего
# print(nam[2::-1]) # [44, 33, 22] c 2 второго символа и до начала
# print(nam[::-1]) #Всё в обратную сторону

# nn = nam
# nn = nam.copy()
# nam[1] = 3333
# #nn = nam[:]
#
# print(nn), print(id(nn))
# print(nam), print(id(nam))
# print(nn is nam)

# print(nam)
# nam.append(100)# Добавить в конец
# nam.append([1,2,5])# Добавить в конец
# nam[5]=250
# nam.insert(0,300) # линейная сложность. Заменяет 0 индекс на 300
# print(nam)
#
# print(nam)
# #nam.extend([1,2,5])
# nam+=[1,2,5] # сокращение
# nam = nam + [1,5,9] #
# print(nam)
#
# nam  = nam.pop(3) # удаляет 3 индекс
# print(nam)

# nam.clear() # Очищает список
# print(nam)

# nam = [22, 33, 44, 55, 99]
# for i in range(len(nam)):
#     print(i, nam[i])
#
# cnt= 0
# for i in enumerate(nam):
#     print( i, end="   ")
# #    cnt+=1
# print()
#
#
# """Кортеж (Tuple)"""
# """Кортеж - неизменяемый набор данных"""
# tp = (22, 33, 44, 55, 99)
# k, *i, z = 7, 5, 6, 8, 98, 555, 254,
# print(k, i, z)
#
#
# names = ["pervi", "vtoroq", "tretii", "chetvertii"]
# #names.reverse()
# names.sort()
# print(names)
#
# for k, i in enumerate(names, 1):
#     print(f"{k}. {i}")
#
# for k, i in zip(names, nam):
#     print(k,i)


arr = [0] *10
print(arr)
for i in range(len(arr)):
    arr[i] = i+1
print(arr)

ls= []
for i in range(10):
    ls.append(i+1)
print(ls)
"""или"""
ls = [i +1 for i in range(10)]
print(ls)

tp = ("login","passworf")
print(tp, id(tp))

buf = list(tp) # Перевели кортеж в список
buf[-1] = "new passworf" # Присвоили новое знаение
tp = tuple(buf) # Перевели список в кортеж
print(tp, id(tp))


"""Левый циклический сдвиг"""
l = [22, 33, 44, 55, 99]
temp = l[0]
n = len(l)
for i in range(n-1):
    l[i]=l[i+1]
l[-1]= temp
print(l) #[33, 44, 55, 99, 22]

temp = l.pop(0)
l.append(temp)
print(l)

# замена местами переменные
x=10
y=15
print(x,y)
z=x
x=y
y=z
print(x,y)

x,y = y,x
print(x,y)












