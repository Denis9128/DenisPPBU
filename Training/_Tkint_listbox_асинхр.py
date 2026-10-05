from tkinter import *

window = Tk()
ld=Listbox(width=15,height=5)
ld.pack()

ld.insert(0, 'Понедельник')
ld.insert(1, 'Вторник')
ld.insert(2, 'Среда')
ld.insert(3, 'Четверг')
ld.insert(4, 'Пятница')
ld.insert(5, 'Суббота')
ld.insert(6, 'Воскресенье')



window.mainloop()