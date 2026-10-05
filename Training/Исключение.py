try:
    a =input("Введите число 1:")
    b =input("Введите число 2:")
    a=int(a)
    b=int(b)

    c=a/b
    print(c)
except (ZeroDivisionError,ValueError):
    print("Ошибка ввода")