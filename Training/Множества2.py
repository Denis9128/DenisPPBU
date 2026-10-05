"""Множество (set) - Неупорядоченный набор уникальных объектов
любые неизменяемые типы данных"""

ls= [22,22,22,33,44,17]
st = set(ls) # уникальные объекты
print(st)
st.clear()
st = {22,33,44,17}
print(st)

st.add("Привет")
print(st)

st.update({2,3,17})
print(st)
n= st.pop() #Удаляет первый элемент
print(n)
print(st)

st.remove(2)
st.discard(3)
print(st)


st1 = {3,4,33}
st2 = {3,4,44}
st3 = {3,4}
res =st1.union(st2) # объединить множество
print(res)

res = st1|st2 # объединить множество
print(res)

res = st1.intersection(st2) #Пересечение множеств выявление одинаковых субъектов
print(res)

res= st1.difference(st2) # вычитание множеств
print(res)

res = st1.symmetric_difference(st2)  # выявлеие симетрии
print(res)

st3 = {3,4}
print(st3.issubset(st2))
print(st1.issuperset(st3))









