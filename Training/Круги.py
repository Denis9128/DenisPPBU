import turtle as t
t.colormode(255)
t.speed(0)


r = input('Введите радиус: ')
r = int(r)
for i in range(3):
    t.color(255,100*i,25)

    t.begin_fill()
    t.circle(r)
    t.end_fill()

    t.penup()
    t.forward(150)
    t.pendown()

t.done()

