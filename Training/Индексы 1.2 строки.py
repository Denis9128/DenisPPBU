s = "Здравствуйте, гости!"
print(s [-5])
print(len(s))
print(s[::2])
print(s[::-1])
print(list(reversed(s)))

# for i in s:
#     print(i, end=" ")
print(s[19])
for i in range(len(s)):
    print(s[i], end=" ")

print(s.index(","))
print(s.isalpha()) # Состоит ли из цифр
print(s.islower()) # Состоит ли только из малентких букв
print(s.isupper()) # Большие буквы
print(s.startswith("З"))
print(s.lower()) # нижний регистр
print(s.upper()) # Верхний регистр
print(s.title()) # Каждое слово с большой буквы)