import math
from tkinter import *
from tkinter.messagebox import showerror


def add(n1, d1, n2, d2):
    n = n1*d2+n2*d1
    d = d1*d2
    return n,d

def sub(n1, d1, n2, d2):
    n = n1*d2-n2*d1
    d = d1*d2
    return n,d

def mult(n1, d1, n2, d2):
    n = n1*n2
    d = d1*d2
    return n,d

def div(n1, d1, n2, d2):
    if d1==0 or d2==0:
        raise ZeroDivisionError ("Ошибка деление на ноль")
    n = n1*d2
    d = n2*d1
    return n,d


def hendler():
    try:
        n1 = int(num1.get())
        d1 = int(den1.get())
        n2 = int(num2.get())
        d2 = int(den2.get())
        operator = oper.get().strip()

        if operator == "+":
            result = add(n1, d1, n2, d2)
        elif operator == "-":
            result = sub(n1, d1, n2, d2)
        elif operator == "*":
            result = mult(n1, d1, n2, d2)
        elif operator == "/":
            result = div(n1, d1, n2, d2)

        nod = math.gcd(result[0], result[1])
        n = int(result[0] / nod)
        d = int(result[1] / nod)

        int_part = ''
        if abs(d) < abs(n):
            int_part = int(n // d)
            n = int(n % d)

        if n == 0:
            n = ''
            d = ''

        if n == d:
            n = ''
            d = ''
            int_part = '1'

        num3.config(text=n)
        den3.config(text=d)
        res_int.config(text=int_part)

    except (ValueError,NameError):
        showerror("Ошибка", "Ошибка ввода")
    except ZeroDivisionError:
        showerror("Ошибка", "Ошибка деление на ноль")


root = Tk()
root.title("Калькулятор дробей")
root.geometry("300x130+600+100")

frame = Frame(root)
frame.pack(pady=10)

num1= Entry(frame, width=2)
num1.config(font=("Arial", 15), justify="center")
num1.grid(row=0,column=0) # grid - сетка разметки

Label(frame, text=chr(8212)*3).grid(row=1,column=0)

den1= Entry(frame, width=2)
den1.config(font=("Arial", 15), justify="center")
den1.grid(row=2,column=0) # grid - сетка разметки

oper = Entry(frame, width=2)
oper.config(font=("Arial", 15), justify="center")
oper.grid(row=1,column=1,padx=5)

num2= Entry(frame, width=2)
num2.config(font=("Arial", 15), justify="center")
num2.grid(row=0,column=2) # grid - сетка разметки

Label(frame, text=chr(8212)*3).grid(row=1,column=2)

den2= Entry(frame, width=2)
den2.config(font=("Arial", 15), justify="center")
den2.grid(row=2,column=2) # grid - сетка разметки

btn = Button(frame,text= '=', command=hendler)
btn.config(font=("Arial", 15), justify="center",width=3)
btn.grid(row=1,column=3, pady=5)

res_int = Label(frame, text='    ',bg = 'light gray', width=2)
res_int.config(font=("Arial", 20), justify="center")
res_int.grid(row=1,column=4, padx=5)


num3= Label(frame, width=2,bg = 'light gray')
num3.config(font=("Arial", 15), justify="center")
num3.grid(row=0,column=5) # grid - сетка разметки

Label(frame, text=chr(8212)*3).grid(row=1,column=5)

den3= Label(frame, width=2,bg = 'light gray')
den3.config(font=("Arial", 15), justify="center")
den3.grid(row=2,column=5) # grid - сетка разметки

root.mainloop()