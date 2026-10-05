import turtle as t
t.color("blue")
#t.right(60)
t.pensize(3) #Толщина линии
t.hideturtle()# Скрыть
t.ht()
for i in range(4, 56,4):

    t.forward(i)
    t.right(90)
t.right(270)
for i in range(52, 0, -4):

    t.forward(i)
    t.right(90)
t.done()