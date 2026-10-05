#Проект бронирование мест
from tkinter import *
from tkinter import messagebox as mb

def book_seat (event=None):
    s = seats_Entry.get().title() # Первый символ с большой буквы
    try:
        if seats[s] == "Свободно":
            seats[s] = "Забронировано"
            update_canvas()
            mb.showinfo('Успех',f'Место {s}, успешно забронировано.')
        else:
            mb.showinfo('Ошибка', f'Место {s}, уже забронировано или не существует.')
    except KeyError:
        mb.showerror('Ошибка',f'Место {s}, не существует.')



def update_canvas():
    canvas.delete('all')
    for i, (seat, status) in enumerate(seats.items()):
        x=i*40+20
        y = 20
        color = 'green' if status == 'Свободно' else 'red'
        canvas.create_rectangle(x,y, x+30, y+30, fill=color)
        canvas.create_text(x+15,y+15, text=seat)

def cansel_booking (event=None):
    s = seats_Entry.get().title() # Первый символ с большой буквы
    try:
        if seats[s] == "Забронировано":
            seats[s] = "Свободно"
            update_canvas()
            mb.showinfo('Забронировано',f'Бронь места {s} отменена.')
        else:
            mb.showinfo('Ошибка', f'Место {s}, не существует или уже свободно.')
    except KeyError:
        mb.showerror('Ошибка',f'Место {s}, не существует.')



window = Tk()
window.title('Бронирование мест')
window.geometry('400x240')

canvas = Canvas(window, width=400, height=60, background='white') # Холст
canvas.pack()

seats = {f"Б{i}": "Свободно" for i in range(1,10)} # Словарь
update_canvas()

seats_Entry = Entry()
seats_Entry.pack(pady=10)
seats_Entry.focus() # фокус по умолчанию
seats_Entry.bind('<Return>', book_seat) # При нажатии на энтер, вызывается функция book_seat

Button(text='Забронировать место', command=book_seat).pack(pady=10)


cansel_seats_Entry = Entry()
# cansel_seats_Entry.pack(pady=10)
# cansel_seats_Entry.bind('<Return>', cansel_booking) # При нажатии на энтер, вызывается функция cansel_booking

btn =Button(text='Отменить бронь', command=cansel_booking).pack(pady=10)

window.mainloop()

