import math
from cmath import sqrt

#s = []
# for x in range(1,10):
#     s.append(x**2)
# print(s)

#s= [x**2 for x in range(1,10) if x>3] # та же запись в одну строку


# even = []
# for x in range(20):
#     if x % 2 == 0:
#         even.append(x)


# even= [x for x in range(20) if x % 2 == 0] # та же запись в одну строку
# print(even)

words = ["Яблоко","Груша","апельсин","Арбуз","Виноград","Мандарин", "арбуз", "абрикос"]
# up = []
# for x in words:
#     up.append(x.upper())

up = [x.upper()  for x in words] # та же запись в одну строку
print(up)

f = []
# for i in words:
#     f.append(i[0])

f = [i[0] for i in words]
f2 = [len(i) for i in words] #длина всех слов
print(f)
print(f2)

n= [1,2,9,58,48,56,58,44]
f = [str(i) for i in n]
print(f)

n= [1,2,9,58,48,56,58,44]
f = [i*2 for i in n if i>5]
print(f)

n= [1,2,9,58,48,56,58,44]
f = [math.sqrt(i) for i in n if i<10]
print(f)

f= [i for i in words if i.startswith("а")] # Выбрать все слова из списка которые начинаются с а.
print(f)

