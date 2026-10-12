from tkinter import *

def handler(x):
    btns[x-1].config(bg='lightgray')


def unbusy(num, row):

    if row <= 3:
        color = 'red'
    elif 4 <= row <= 6:
        color = 'blue'
    else:
        color = 'yellow'

    btns[num - 1].config(bg = color)


image= '2.ico'

root = Tk()
root.title('Бронирование')
root.geometry('800x450')
root.iconbitmap(image)


frame1 = Frame(root)
frame1.pack(pady=10)
frame2 = Frame(root)
frame2.pack(pady=10)

screen = Label(frame1, text='Экран')
screen.pack()

canvas = Canvas(frame1, width=400, height=60)
canvas.pack()

canvas.create_line(50,10,350,10, fill='lightblue', width=8)
canvas.create_line(60,40,140,40, fill='red', width=4)
canvas.create_text(100,30, text='1500')
canvas.create_line(160,40,240,40, fill='blue', width=4)
canvas.create_text(200,30, text='1200')
canvas.create_line(260,40,340,40, fill='yellow', width=4)
canvas.create_text(300,30, text='1000')

# btn1 = Button(frame2)
# btn1.config(text=1, font=('Arial', 10), bg='red',justify='center', width=2, command=lambda x= btn1: handler(x))
# btn1.grid(row=0, column=0)
#
# btn2 = Button(frame2)
# btn2.config(text=2, font=('Arial', 10), bg='red',justify='center', width=2, command=lambda x= btn2: handler(x))
# btn2.grid(row=0, column=1)


row = 10
colomn = 18

btns = []

for i in range(row):
    Label(frame2, text=f'Ряд - {i + 1}').grid(row=i, column=0)

    for j in range(colomn):
        num = i *colomn + j + 1
        if i <=3:
            color = 'red'
        elif 4<= i <=6:
            color = 'blue'
        else:
            color = 'yellow'
        btn = Button(frame2)
        btn.config(text=f'{j + 1}', font=('Arial', 10), bg=color,justify='center', width=2, command=lambda x= num: handler(x))
        btn.grid(row = i, column = j + 1,padx=0.4, pady=0.4)

        btn.bind('<Button-3>', lambda event, nm = num, r=i: unbusy(nm, r))

        btns.append(btn)






root.mainloop()