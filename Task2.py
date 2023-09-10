
from tkinter import*
import math


t=Tk()
t.title("Simple Calculator")
t.config(bg="Black")
l=Entry(t,width="65",borderwidth="4",bg="lightblue")
l.grid(row=0,column=0,columnspan=7,padx=10,pady=10)

def clk(number):
    a=l.get()
    l.delete(0, END)
    l.insert(0, str(a)+str(number))

def clr():
    l.delete(0,END)

def add():
    fn=l.get()
    global fnum
    global js
    js="Addition"
    fnum= int(fn)
    l.delete(0,END)

def eql():
    scdn=l.get()
    l.delete(0,END)
    
    if js=="Addition":
        l.insert(0, fnum + int(scdn))
    if js=="Subtraction":
        l.insert(0, fnum-int(scdn))
    if js=="Multiplication":
        l.insert(0,fnum * int(scdn))
    if js=="Division":
        l.insert(0,fnum/int(scdn))
    if js=="SQRT":
        l.insert(0,math.sqrt(fnum))
    if js=="Square":
        l.insert(0,fnum*fnum)
    if js=="sin":
        ang=math.radians(fnum)
        l.insert(0,math.sin(ang))
    l.focus_set()


def sub():
    fn = l.get()
    global fnum
    global js
    js = "Subtraction"
    fnum = int(fn)
    l.delete(0, END)


def mul():
    fn = l.get()
    global fnum
    global js
    js = "Multiplication"
    fnum = int(fn)
    l.delete(0, END)

def div():
    fn = l.get()
    global fnum
    global js
    js = "Division"
    fnum = int(fn)
    l.delete(0, END)

def ded():
    da=l.get()
    if da:
        ns=da[:-1]
        l.delete(0,END)
        l.insert(0,ns)


def sq():
    fn = l.get()
    global fnum
    global js
    js = "Square"
    fnum = int(fn)

    l.insert(0,fnum*fnum)
    l.delete(0,END)
def sqrt():
    fn = l.get()
    global fnum
    global js
    js = "SQRT"
    fnum = int(fn)
    l.delete(0, END)

def sin():
    fn = l.get()
    global fnum
    global js
    js = "sin"
    fnum = float(fn)
    l.delete(0, END)


btn1=Button(t,text="1",padx=40,pady=20,command= lambda: clk(1),bg="lightgreen")
btn2=Button(t,text="2",padx=40,pady=20,command= lambda: clk(2),bg="lightgreen")
btn3=Button(t,text="3",padx=40,pady=20,command= lambda: clk(3),bg="lightgreen")
btn4=Button(t,text="4",padx=40,pady=20,command= lambda: clk(4),bg="lightgreen")
btn5=Button(t,text="5",padx=40,pady=20,command= lambda: clk(5),bg="lightgreen")
btn6=Button(t,text="6",padx=40,pady=20,command= lambda: clk(6),bg="lightgreen")
btn7=Button(t,text="7",padx=40,pady=20,command= lambda: clk(7),bg="lightgreen")
btn8=Button(t,text="8",padx=40,pady=20,command= lambda: clk(8),bg="lightgreen")
btn9=Button(t,text="9",padx=40,pady=20,command= lambda: clk(9),bg="lightgreen")
btn0=Button(t,text="0",padx=40,pady=20,command= lambda: clk(0),bg="lightgreen")
btnad=Button(t,text="+",padx=42,pady=20,command= lambda: add(),bg="lightgreen")
btnsub=Button(t,text="-",padx=43,pady=20,command= lambda: sub(),bg="lightgreen")
btndiv=Button(t,text="/",padx=43,pady=20,command= lambda: div(),bg="lightgreen")
butnmul=Button(t,text="x",padx=43,pady=20,command= lambda: mul(),bg="lightgreen")
btneq=Button(t,text="=",padx=40,pady=20,command= lambda: eql(),bg="lightgreen")
btnclr=Button(t,text="CLR",padx=32,pady=20,command= lambda: clr(),bg="lightgreen")
btndel=Button(t,text="Del",padx=35,pady=20,command= lambda: ded(),bg="lightgreen")
btnsq=Button(t,text="^2",padx=37,pady=20,command=lambda: sq(),bg="lightgreen")
btnsqrt=Button(t,text="√",padx=40,pady=20,command=lambda: sqrt(),bg="lightgreen")
btnsin=Button(t,text="Sin",padx=35,pady=20,command=lambda: sin(),bg="lightgreen")



btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn7.grid(row=3,column=0)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)

btnclr.grid(row=4,column=0)
btn0.grid(row=4,column=1)
btneq.grid(row=4,column=2)


btnad.grid(row=4,column=3)
btnsub.grid(row=3,column=3)
butnmul.grid(row=2,column=3)
btndiv.grid(row=1,column=3)

btndel.grid(row=1,column=5)
btnsq.grid(row=2,column=5)
btnsqrt.grid(row=3,column=5)
btnsin.grid(row=4,column=5)


t.mainloop()
