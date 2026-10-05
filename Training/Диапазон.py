import turtle as t
t.speed(0)
t.colormode(255)
t.pensize(2)


# Эта программа рисует круги

#print(range(2,10))


for i in range(30,120):
   t.color(2*i,120,255)
   t.circle(i)
   t.lt(45)

t.done()