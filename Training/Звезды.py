import turtle as t
#turtle.shape("turtle")
t.ht()
ugol = 10
t.color('pink')
t.begin_fill()
for i in range(ugol):
    #print(i)
    t.forward(150)
    t.right(360 *3/ ugol)
t.end_fill()
t.done()