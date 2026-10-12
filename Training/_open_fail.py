# file = open('text.txt', 'r', encoding='utf-8')
#
# sl = file.readlines()
# print(sl)
#
# file.close()

# for i in open('text.txt', 'r', encoding='utf-8'):
#     print(i.rstrip())

# with open('text.txt', 'r', encoding='utf-8') as f: # Для чтения
#      ls= f.read().title().split()
# ls.sort()
# print(ls)

with open('text1.txt', 'w', encoding='utf-8') as file:# Для записи
    for n, f in enumerate(ls, 1):
        file.write(f'{n}, {f}\n')
        print(n,f)

# with open('text.txt', 'a', encoding='utf-8') as f:  # Дописать в файл
