from tkinter import *

window = Tk()
ld=Listbox(width=15,height=7)
ld.pack()

days = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
for day in days:
    ld.insert(END,day) # Вставить в конец элемент из списка

window.mainloop()