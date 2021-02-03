from tkinter import *
import math
screen = Tk()
screen.title('My Simple Calculator')
screen.maxsize(width=450,height=450)
screen.minsize(width=365,height=450)
screen.configure(bg='powder blue')
screen.geometry('360x485')

screen.iconbitmap('cal.ico')

def click(number):
    global operator
    operator += str(number)
    t.set(operator)

def clear():
    global operator
    operator = ''
    t.set(operator)


def equal():
    global operator
    res = eval(operator)
    operator= str(res)
    t.set(operator)

def cmsin():
    global operator
    res=math.sin(eval(t.get()))
    operator=str(res)
    t.set(operator)

def cmcos():
    global operator
    res = math.cos(eval(t.get()))
    operator = str(res)
    t.set(operator)

def cmtan():
    global operator
    res = math.tan(eval(t.get()))
    operator = str(res)
    t.set(operator)

def cmsqrt():
    global operator
    res = math.sqrt(eval(t.get()))
    operator = str(res)
    t.set(operator)

def cmlog():
    global operator
    res = math.log(eval(t.get()))
    operator = str(res)
    t.set(operator)



t = StringVar()
operator = ''

entryBox = Entry(screen, bg='#FFA07A', font=('open sans', 20, 'italic bold'), bd=28, justify='right', textvariable=t)
entryBox.grid(row=0, columnspan=4)

#row0

btnSin = Button(screen, text='sin', font=('open sans', 15, 'italic bold'), bd=8, padx=30, pady=20
              , command=cmsin, activebackground='#90EE90')
btnSin.grid(row=0, column=4)

# row1

btn7 = Button(screen, text='7', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
              , command=lambda: click(7), activebackground='#90EE90')
btn7.grid(row=1, column=0)

btn8 = Button(screen, text='8', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
              , command=lambda: click(8), activebackground='#90EE90')
btn8.grid(row=1, column=1)

btn9 = Button(screen, text='9', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
              , command=lambda: click(9), activebackground='#90EE90')
btn9.grid(row=1, column=2)

btnPlus = Button(screen, text='+', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
                 ,command=lambda:click('+'), activebackground='#90EE90')
btnPlus.grid(row=1, column=3)

btnCos = Button(screen, text='cos', font=('open sans', 15, 'italic bold'), bd=8, padx=30, pady=20
              , command=cmcos, activebackground='#90EE90')
btnCos.grid(row=1, column=4)

# row2

btn4 = Button(screen, text='4', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
              , command=lambda: click(4), activebackground='#90EE90')
btn4.grid(row=2, column=0)

btn5 = Button(screen, text='5', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
              , command=lambda: click(5), activebackground='#90EE90')
btn5.grid(row=2, column=1)

btn6 = Button(screen, text='6', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
              , command=lambda: click(6), activebackground='#90EE90')
btn6.grid(row=2, column=2)

btnMinus = Button(screen, text='-', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
                  ,command=lambda:click('-'), activebackground='#90EE90')
btnMinus.grid(row=2, column=3)

btnTan = Button(screen, text='tan   ', font=('open sans', 15, 'italic bold'), bd=8, padx=25, pady=20
              , command=cmtan, activebackground='#90EE90')
btnTan.grid(row=2, column=4)

# row3

btn1 = Button(screen, text='1', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
              , command=lambda: click(1), activebackground='#90EE90')
btn1.grid(row=3, column=0)

btn2 = Button(screen, text='2', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
              , command=lambda: click(2), activebackground='#90EE90')
btn2.grid(row=3, column=1)

btn3 = Button(screen, text='3', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
              , command=lambda: click(3), activebackground='#90EE90')
btn3.grid(row=3, column=2)

btnMulti = Button(screen, text='*', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
                  ,command=lambda:click('*'), activebackground='#90EE90')
btnMulti.grid(row=3, column=3)

btnSqrt = Button(screen, text='sqrt', font=('open sans', 13, 'italic bold'), bd=8, padx=30, pady=25
              , command=cmsqrt, activebackground='#90EE90')
btnSqrt.grid(row=3, column=4)

# row4


btn0 = Button(screen, text='0', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20
              , command=lambda: click(8), activebackground='#90EE90')
btn0.grid(row=4, column=0)

btnClear = Button(screen, text='C', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20, command=clear
                  , activebackground='#90EE90')
btnClear.grid(row=4, column=1)

btnEqual = Button(screen, text='=', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20, command=equal
                  , activebackground='#90EE90')
btnEqual.grid(row=4, column=2)

btnDiv = Button(screen, text='/', font=('open sans', 15, 'italic bold'), bd=8, padx=20, pady=20,command=lambda:click('/')
                , activebackground='#90EE90')
btnDiv.grid(row=4, column=3)

btnLog = Button(screen, text='log', font=('open sans', 15, 'italic bold'), bd=8, padx=30, pady=18
              , command=cmlog, activebackground='#90EE90')
btnLog.grid(row=4, column=4)

screen.mainloop()
