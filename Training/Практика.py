import turtle as t #Вложенные циклы
import time # импорт блока времени
t.speed(0) #Скорость черепахи
t.penup()
t.forward(-150)
t.pendown()
t.hideturtle()
r = 40
t.pensize(3)
t.color("#FF513D")
t.fillcolor("#274DEA")
for k in range(3):
    print("________k = "+str(k))
    for g in range(4):
        print("___g = "+str(g))
        for i in range(6):
            print("i = " +str(i))
            t.begin_fill()
            t.circle(r)
            t.end_fill()
            t.right(60)
            time.sleep(0.1) #Время работы
        r= r-10

    t.penup()
    t.forward(160)
    t.pendown()
    r=40



t.done()