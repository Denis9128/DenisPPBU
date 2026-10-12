with open('text.txt', 'r', encoding='utf-8') as file:
    s = file.read()
    key = input('Введите ключ шифрования: ' )
    secrets = ''
    for c in s:
        # if c == key:
        code = ord(c) + int(key)
        symbol = chr(code)
        secrets += symbol
print('текст зашифрован')

with open('code.txt', 'w', encoding='utf-8') as file:
    file.write(secrets)

print('Сформирован code.txt')