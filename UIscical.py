from tkinter import *

app = Tk()
displayColor = "#85754a"
backColor = "#1e0547"

display = Frame(app, bg=displayColor, width=555, height=230)
display.place(x=50, y=20)
maintitle = Label(text="Scientific Calculator", font=("Arial", 10), background=backColor, foreground="red")
maintitle.pack(side="top")
ent = Label(display, text="", font=("Arial", 30), bg=displayColor, anchor="w")
ent.place(anchor="nw")
ans = Label(display, text="", font=("Arial", 30), bg=displayColor, anchor="e")
ans.place(relx=1, rely=1, anchor="se", width=540)
center = Frame(app, width=555, height=500)
center.place(x=50, y=275)

#0
def wrzero():
    current = ent.cget("text")
    ent.config(text= current + "0")

zerobt = Button(center, text="0", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrzero)
zerobt.place(x=12, y=430)

#1
def wrone():
    current = ent.cget("text")
    ent.config(text=current + "1")

onebt = Button(center, text="1", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrone)
onebt.place(x=12, y=360)

#2
def wrtwo():
    current = ent.cget("text")
    ent.config(text=current + "2")

twobt = Button(center, text="2", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrtwo)
twobt.place(x=102, y=360)

#3
def wrthree():
    current = ent.cget("text")
    ent.config(text=current + "3")

threebt = Button(center, text="3", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrthree)
threebt.place(x=192, y=360)

#4
def wrfour():
    current = ent.cget("text")
    ent.config(text=current + "4")

fourbt = Button(center, text="4", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrfour)
fourbt.place(x=12, y=290)

#5
def wrfive():
    current = ent.cget("text")
    ent.config(text=current + "5")

fivebt = Button(center, text="5", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrfive)
fivebt.place(x=102, y=290)

#6
def wrsix():
    current = ent.cget("text")
    ent.config(text=current + "6")

sixbt = Button(center, text="6", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrsix)
sixbt.place(x=192, y=290)

#7
def wrseven():
    current = ent.cget("text")
    ent.config(text=current + "7")

sevenbt = Button(center, text="7", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrseven)
sevenbt.place(x=12, y=220)

#8
def wreight():
    current = ent.cget("text")
    ent.config(text=current + "8")

eightbt = Button(center, text="8", font=("Arial", 22), bg="black", foreground="white", width=4, command=wreight)
eightbt.place(x=102, y=220)

#9
def wrnine():
    current = ent.cget("text")
    ent.config(text=current + "9")

ninebt = Button(center, text="9", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrnine)
ninebt.place(x=192, y=220)

#+
def plus():
    current = ent.cget("text")
    ent.config(text=current + "+")

plusbt = Button(center, text="+", font=("Arial", 22), bg="black", foreground="white", width=4, command=plus)
plusbt.place(x=282, y=360)

#-
def minus():
    current = ent.cget("text")
    ent.config(text=current + "-")

minusbt = Button(center, text="-", font=("Arial", 22), bg="black", foreground="white", width=4, command=minus)
minusbt.place(x=372, y=360)

#*
def multi():
    current = ent.cget("text")
    ent.config(text=current + "*")

minusbt = Button(center, text="x", font=("Arial", 22), bg="black", foreground="white", width=4, command=multi)
minusbt.place(x=282, y=290)

#=
def result():
    current = ent.cget("text")
    res = eval(current)
    ans.config(text=f"{res}")

resultbt = Button(center, text="=", font=("Arial", 22), bg="black", foreground="white", width=4, command=result)
resultbt.place(x=102, y=430)

app.configure(bg=backColor)
app.geometry("650x800")
app.title("Scientific Calculator")
app.mainloop()
