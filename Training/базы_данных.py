import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()


# cursor.execute('''INSERT INTO Car (name, model, yaear, activ) # Добавить в БД
#                   VALUES (?, ?, ?,?)
#  ''', ('VAZ',2106, 1987,1)) # То что добавляем

# cursor.execute('''UPDATE Car set name = 'Lada' WHERE ID = 3''') # оБНОВИТЬ ДАННЫМИ
# DELETE From Car WHERE ID = 5;


conn.commit()

# result = cursor.execute('''SELECT * FROM Car WHERE ID = 3''')
# result = cursor.execute('''SELECT * FROM Car''') # Все данные
# result = cursor.execute('''SELECT name, model FROM Car''') # Нужные колонки
# result = cursor.execute('''SELECT name, model FROM Car WHERE model = "X-Treil"''') # Нужные колонки
# result = cursor.execute('''SELECT name, model FROM Car WHERE name LIKE "V%"''') # Нужные колонки По началу символов
# result = cursor.execute('''SELECT DISTINCT name FROM Car''') # Получить уникальные имена
result = cursor.execute('''SELECT name, model FROM Car WHERE yaear BETWEEN 2019  and 2020 ORDER BY name DESC;''') # Показать все с 2019 и 2020 год
# print(result)
for row in result:
    print(row)