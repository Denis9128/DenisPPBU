import turtle as t
t.speed(0)
t.hideturtle()
t.pensize(3)


for j in range(60, 0, -10):
    for i in range(6):
        t.color("green")
        t.fillcolor("red")

        t.begin_fill()
        t.circle(j)
        t.end_fill()
        t.rt(60)


t.done()



