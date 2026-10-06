from tkinter import *

pen_color = 'black'

def draw(event):
    x,y = event.x,event.y
    canvas.create_oval(x,y,x+5,y+5,fill=pen_color,outline=pen_color)


window = Tk()
window.title("Графический редактор")

canvas = Canvas(width=600, height=400)
canvas.pack()
canvas.bind('<B1-Motion>', draw)

# colors= ['red','grin','blue','black']
# for color in colors:
#     lbl = Label(text=colors, width=8, height=2)
#     lbl.pack()
#     lbl.bind('<B1-Motion>', lambda e, c=color: globals().update(pen_color=c))



window.mainloop()