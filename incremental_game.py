from tkinter import *
import time

r = Tk()
start = time.time()

r.title("incremental game")

r.geometry("414x736")
r.minsize(414, 736)
r.maxsize(414, 736)

mainTitle = Label(r, text="v0.0.1-alpha")
mainTitle.pack()

money = float()
gatherers = int()
miners = int()
dps = float()

def reset():
    global money
    global gatherers
    global miners
    global dps
    money = 0.0
    moneyLabel.configure(text=""+str(money)+ " dollars")
    gatherers = 0
    gathererLabel.configure(text=""+str(gatherers)+ " gatherers")
    miners = 0
    minerLabel.configure(text=""+str(miners)+" miners")
    dps = 0.0
    ppsLabel.configure(text="dps: "+str(dps))

def exit():
    r.destroy()
    
menu = Menu(r)
r.config(menu=menu)
fileMenu = Menu(menu, tearoff="off")
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Reset", command=reset)
fileMenu.add_command(label="Exit", command=exit)

def click1():
    global money
    money += 1
    moneyLabel.configure(text=""+str(money)+" dollars")

def buygatherers():
    global gatherers
    global money
    if money >= 10:
        gatherers += 1
        money = money - 10
        moneyLabel.configure(text=""+str(money)+" dollars")
        gathererLabel.configure(text=""+str(gatherers)+" gatherers")
    else:
        gatherers += 0
        gathererLabel.configure(text=""+str(gatherers)+" gatherers")

button1 = Button(r, command=click1, text="CLICK")
button1.place(relx=0.5, rely=0.1, anchor="center")

moneyLabel = Label(r, text=""+str(money)+" dollars")
moneyLabel.place(relx=0.5, rely=0.05, anchor="center")

ppsLabel = Label(r, text="dps: "+str(dps))
ppsLabel.place(relx=0.75, rely=0.05, anchor="center")

def ppscheck():
    global dps
    if gatherers >= 1 or miners >= 1:
        dps = gatherers + 2.5*miners
        ppsLabel.configure(text="dps: "+str(dps))
    else:
        ppsLabel.configure(text="dps: "+str(dps))
    r.after(5,ppscheck)

r.after(5,ppscheck)

button2 = Button(r, command=buygatherers, text="BUY 1")
button2.place(relx=0.5, rely=0.15, anchor="center")

gathererLabel = Label(r, text=""+str(gatherers)+" gatherers")
gathererLabel.place(relx=0.25, rely=0.15, anchor="w")

def gathererpps():
    global money
    global gatherers
    if gatherers >= 1:
        money += 1 * gatherers
        moneyLabel.configure(text=""+str(money)+" dollars")
    else: 
        money += 0
    r.after(1000, gathererpps)

r.after(1000,gathererpps)

def buyminers():
    global money
    global miners
    if money >= 50:
        miners += 1
        minerLabel.configure(text=""+str(miners)+" miners")
        money = money - 50
    else:
        miners += 0

button3 = Button(r, command=buyminers, text="BUY 1")
button3.place(relx=0.5, rely=0.20, anchor="center")

minerLabel = Label(r, text=""+str(miners)+" miners")
minerLabel.place(relx=0.25, rely=0.20, anchor="w")

def minerpps():
    global money
    global miners
    if miners >= 1:
        money += 2.5
        moneyLabel.configure(text=""+str(money)+" dollars")
    else:
        money += 0
    r.after(1000, minerpps)

r.after(2000,minerpps)

r.mainloop()