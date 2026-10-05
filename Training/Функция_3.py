def num2(n:int)->None:
    if n>1:
        num2(n- 1)
    print(n)

def num1(n:int)->None:
    if n>1:
        num2(n- 1)
    print(n)

def num(n:int)->None:
    if n>1:
        num1(n- 1)
    print(n)
num(4)