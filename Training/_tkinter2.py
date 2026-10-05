from tkinter import *

#from webencodings import labels

def answer(event=None):
    answ = num.get().strip() # get() - получает данные strip()- удаляет данные начала и конца строки
    result.configure(text=answ)

root = Tk() # Создаём основное окно
root.title("Старт")

WIDTH = root.winfo_screenwidth() # Размер экрана
HEIGHT = root.winfo_screenheight()  #Размер экрана
X = 300 #Размер окна
Y = 150 #Размер окна

root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
              f"+{HEIGHT // 2 - Y // 2 - 25}")

#root.geometry("300x300+400+200")


promt = Label(text="Введите значение", font = "Arial 15",justify='center')
promt.pack() # Размещаем виджет в окне

num = Entry(width=10, font="Arial 15", justify='right') # Создаём окно для ввода
num.pack() # Размещаем виджет в окне

result = Label(text = " ", font="Arial 15", bg ="light grey")

result.pack(pady=10) # Размещаем виджет в окне отступ 10

btn = Button(text="Введите значение", command=answer)
btn.pack(pady=10)

num.bind("<Return>", answer)

root.mainloop() # Запускаем цикл событий

