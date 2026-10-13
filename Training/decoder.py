with open('code.txt', 'r', encoding='utf-8') as file:
    s = file.read()
    key = input('Введите ключ шифрования: ' )
    unsecrets = ''
    for c in s:
        code = ord(c) - int(key)
        symbol = chr(code)
        unsecrets += symbol
print('Текст расшифрован')

with open('decode.txt', 'w', encoding='utf-8') as file:
    file.write(unsecrets)

print('Сформирован фаил decode.txt')