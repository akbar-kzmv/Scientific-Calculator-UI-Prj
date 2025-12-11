from tkinter import *

app = Tk()
displayColor = "#85754a"
backColor = "#1e0547"
dangColor = "#8f1426"

display = Frame(app, bg=displayColor, width=555, height=230)
display.place(x=50, y=20)
maintitle = Label(text="Scientific Calculator", font=("Arial", 13), background=backColor, foreground="red")
maintitle.pack(side="top")
ent = Entry(display, font=("Arial", 30), bg=displayColor, foreground="black", insertbackground="black", insertwidth=3)
ent.focus_set()
ent.place(anchor="nw")
ans = Label(display, text="", font=("Arial", 30), bg=displayColor, anchor="e")
ans.place(relx=1, rely=1, anchor="se", width=540)
center = Frame(app, width=555, height=500)
center.place(x=50, y=275)

#0
def wrzero():
    pos = ent.index(INSERT)
    ent.insert(pos, "0")

zerobt = Button(center, text="0", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrzero)
zerobt.place(x=12, y=430)

#leftcursor
def cursor_left():
    ent.icursor(ent.index(INSERT) - 1)
leftbt = Button(center, text="LF", font=("Arial", 22), bg="black", foreground="white", width=4, command=cursor_left)
leftbt.place(x=460, y=430)

#rightcursor
def cursor_right():
    ent.icursor(ent.index(INSERT) + 1)
rightbt = Button(center, text="LR", font=("Arial", 22), bg="black", foreground="white", width=4, command=cursor_right)
rightbt.place(x=460, y=370)

#1
def wrone():
    pos = ent.index(INSERT)
    ent.insert(pos, "1")

onebt = Button(center, text="1", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrone)
onebt.place(x=12, y=360)

#2
def wrtwo():
    pos = ent.index(INSERT)
    ent.insert(pos, "2")

twobt = Button(center, text="2", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrtwo)
twobt.place(x=102, y=360)

#3
def wrthree():
    pos = ent.index(INSERT)
    ent.insert(pos, "3")

threebt = Button(center, text="3", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrthree)
threebt.place(x=192, y=360)

#4
def wrfour():
    pos = ent.index(INSERT)
    ent.insert(pos, "4")

fourbt = Button(center, text="4", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrfour)
fourbt.place(x=12, y=290)

#5
def wrfive():
    pos = ent.index(INSERT)
    ent.insert(pos, "5")

fivebt = Button(center, text="5", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrfive)
fivebt.place(x=102, y=290)

#6
def wrsix():
    pos = ent.index(INSERT)
    ent.insert(pos, "6")

sixbt = Button(center, text="6", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrsix)
sixbt.place(x=192, y=290)

#7
def wrseven():
    pos = ent.index(INSERT)
    ent.insert(pos, "7")

sevenbt = Button(center, text="7", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrseven)
sevenbt.place(x=12, y=220)

#8
def wreight():
    pos = ent.index(INSERT)
    ent.insert(pos, "8")

eightbt = Button(center, text="8", font=("Arial", 22), bg="black", foreground="white", width=4, command=wreight)
eightbt.place(x=102, y=220)

#9
def wrnine():
    pos = ent.index(INSERT)
    ent.insert(pos, "9")

ninebt = Button(center, text="9", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrnine)
ninebt.place(x=192, y=220)

#+
def plus():
    pos = ent.index(INSERT)
    ent.insert(pos, "+")

plusbt = Button(center, text="+", font=("Arial", 22), bg="black", foreground="white", width=4, command=plus)
plusbt.place(x=282, y=360)

#-
def minus():
    pos = ent.index(INSERT)
    ent.insert(pos, "-")

minusbt = Button(center, text="-", font=("Arial", 22), bg="black", foreground="white", width=4, command=minus)
minusbt.place(x=372, y=360)

#*
def multi():
    pos = ent.index(INSERT)
    ent.insert(pos, "*")

multibt = Button(center, text="x", font=("Arial", 22), bg="black", foreground="white", width=4, command=multi)
multibt.place(x=282, y=290)

#=
def result():
    try:
        current = ent.cget("text")
        res = eval(current)
        ans.config(text=f"{res}", foreground="black")
    except Exception:
        ans.config(text="Enter a true value", foreground=dangColor)

resultbt = Button(center, text="=", font=("Arial", 22), bg="black", foreground="white", width=4, command=result)
resultbt.place(x=102, y=430)

#del
def delete():
    pos = ent.index(INSERT)
    ent.delete(pos - 1)
    ent.icursor(pos - 1)

delbt = Button(center, text="DEL", font=("Arial", 22), bg="black", foreground="white", width=4, command=delete)
delbt.place(x=282, y=220)

def AC():
    ent.delete(0, END)

acbt = Button(center, text="AC", font=("Arial", 22), bg="black", foreground="white", width=4, command=AC)
acbt.place(x=372, y=220)

#(
def lftbracket():
    pos = ent.index(INSERT)
    ent.insert(pos, "(")

lftbracketbt = Button(center, text="(", font=("Arial", 22), bg="black", foreground="white", width=4, command=lftbracket)
lftbracketbt.place(x=192, y=430)

#)
def rgtbracket():
    pos = ent.index(INSERT)
    ent.insert(pos, ")")

rgtbracketbt = Button(center, text=")", font=("Arial", 22), bg="black", foreground="white", width=4, command=rgtbracket)
rgtbracketbt.place(x=282, y=430)

#dot
def wrdot():
    pos = ent.index(INSERT)
    ent.insert(pos, ".")

dotbt = Button(center, text=".", font=("Arial", 22), bg="black", foreground="white", width=4, command=wrdot)
dotbt.place(x=372, y=430)

def block(k):
    return "Block!"
ent.bind("<Key>", block)

app.configure(bg=backColor)
app.geometry("650x800")
app.title("Scientific Calculator")
app.mainloop()
