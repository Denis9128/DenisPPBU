import turtle
turtle.shape("turtle")


ugol = input("Введите количество углов:")
ugol = int(ugol)

Col = input('Введите цвет:')
turtle.color(Col)

turtle.begin_fill()
for i in range(ugol):
    #print(i)
    turtle.forward(15)
    turtle.left(360 / ugol)
turtle.end_fill()
turtle.done()
