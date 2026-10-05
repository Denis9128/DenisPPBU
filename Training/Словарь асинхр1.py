d = {"name":"Алиса", "age":15}
d2 = {"school":"Школа 2005", "pet":"Маркус"}
#d["school"] = "Школа 2005"


# print(d["name"])
# print(d)
#
# # del d["age"]
# # print(d)
#
# if "name" in d:
#     print(f"{d["name"]}, есть в словаре")
# else:
#     print("Нет в словаре")
#
# for i in d.values(): # Перебрать все значения
#     print(i)
#
# for t, v in d.items(): # Перебрать все значения
#     print(t,v , end=" ")

d.update(d2) #Слияние словарей
print(d)