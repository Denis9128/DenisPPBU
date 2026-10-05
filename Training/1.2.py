from turtle import *
colormode(255)
pensize(3)
r = 255
g = 255
b = 0
color("green", (r,g,b))
speed(0)

for j in range(150, 10, -25):
    color("red", (r,g,b))
    for i in range(8):
        color("red", (r,g,b))
        begin_fill()
        circle(j)
        end_fill()
        right(45)
    r =58
    g -=5*i
    b =5


mainloop()

