# def sumr (a,y):
#     z=12
#     z+=3
#     print("x=" ,x,y,"Z =",z)
#     return x
#
# z= 1000
# x= 5000
#
# res = sumr(10,20)
# print(res)
# print("x=" ,x, "Z =",z)

def is_eval(n: int) -> bool:
    """Определяет четность числа"""
    return n %2 ==0

print(is_eval.__doc__)
print(is_eval(3))

# def choice_eval(x:int,y:int) -> None:
#     """Выбирает четные числа из последовательности"""
#     for i in range(x,y+1):
#         if is_eval(i):
#             print(i, end = " ")
#
# choice_eval(100,140)


for n in range(100,200):
    for i in range (2,n):
        if n % i == 0:
            break
    else:
        print(n, end = " ")







