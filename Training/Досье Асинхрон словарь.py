d = {
    "name":"Алексей",
     "age":30,
     "prof":"Программист",
     "edu":"МГУ",
     "lang":["русский", "английский"]
}
for k,v in d.items():
    if isinstance(v, list):
        v =",".join(v) # преобразовывает из списка встроку
    print(f"{k} \t{v}")