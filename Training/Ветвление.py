n = input("Введите число:")

if n.isdigit() or (n[0]=="-" and n[1:].isdigit()):
    n = int(n)
    if n>0:
        print("Число положительное")
    elif n<0:
        print("Число отрицательное")
    else:
        print("Число 0")
else:
    print(f"{n} - Это не число")
