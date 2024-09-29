from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class CivCremental(Tk):
    def __init__(self):
        super().__init__()

        self.title('CivCremental')
        self.geometry('414x736')
        self.minsize(414, 736)
        self.maxsize(414, 736)

        self.money = 0.0
        self.dps = 0.0
        self.gatherers = 0
        self.gatherersPrice = 10.0
        self.gathererstickspeed = 1000
        self.miners = 0
        self.minersPrice = 50.0
        self.refiners = 0
        self.refinersPrice = 100.0
        self.mbresearch = 0
        self.firediscovery = 0

        self.create_widgets()

    def create_widgets(self):
        self.mainTitle = Label(self, text='Version: v0.0.2-alpha')
        self.mainTitle.pack()

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill='both')

        self.frame1 = ttk.Frame(notebook, width=414, height=736)
        self.frame2 = ttk.Frame(notebook, width=414, height=736)
        self.frame3 = ttk.Frame(notebook, width=414, height=736)

        notebook.add(self.frame1, text='Money Generation')
        notebook.add(self.frame2, text='Research')
        notebook.add(self.frame3, text='Discovery')

        self.create_frame1()
        self.create_frame2()
        self.create_frame3()

        self.update_buttons()
        self.update_dps()
        self.update_money_generation()

    def create_frame1(self):
        #display & price labels: anchor='w'
        #buttons & dps labels: anchor='center'

        #money (display, button, respectively)
        self.moneyLabel = Label(self.frame1, text=f'Net Worth: ${self.money}')
        self.moneyLabel.place(relx=0.5, rely=0.035, anchor='center')

        self.moneyclicker = Button(self.frame1, command=self.clicker, text='CLICK')
        self.moneyclicker.place(relx=0.5, rely=0.075, anchor='center')

        #gatherers (display, price, dps, sprite, button, respectively)
        self.gatherersLabel = Label(self.frame1, text=f'{self.gatherers} gatherers')
        self.gatherersLabel.place(relx=0.10, rely=0.15, anchor='w')

        self.gatherersPLabel = Label(self.frame1, text=f'${self.gatherersPrice}')
        self.gatherersPLabel.place(relx=0.3, rely=0.15, anchor='w')

        self.gatherersDPSLabel = Label(self.frame1, text='Generates 1dps')
        self.gatherersDPSLabel.place(relx=0.8, rely=0.15, anchor='center')

        self.gathererssprite = Image.open('sprites\\sprite_0.png')
        self.gathererssprite = ImageTk.PhotoImage(self.gathererssprite)

        self.gatherersButton = Button(self.frame1, command=self.buy_gatherers, image=self.gathererssprite, state=DISABLED)
        self.gatherersButton.place(relx=0.5, rely=0.15, anchor='center')

        #miners (display, price, dps, sprite, button, respectively)
        self.minersLabel = Label(self.frame1, text=f'{self.miners} miners')
        self.minersLabel.place(relx=0.1, rely=0.225, anchor='w')

        self.minersPLabel = Label(self.frame1, text=f'${self.minersPrice}')
        self.minersPLabel.place(relx=0.3, rely=0.225, anchor='w')

        self.minersDPSLabel = Label(self.frame1, text='Generates 2.5dps')
        self.minersDPSLabel.place(relx=0.8085, rely=0.225, anchor='center')

        self.minerssprite = Image.open('sprites\\sprite_1.png')
        self.minerssprite = ImageTk.PhotoImage(self.minerssprite)

        self.minersButton = Button(self.frame1, command=self.buy_miners, image=self.minerssprite, state=DISABLED)
        self.minersButton.place(relx=0.5, rely=0.225, anchor='center')

        #refiners @ 'discoverfire()' func

        #dev stuff
        self.devButton = Button(self.frame1, text='add $10000', command=self.devfunc)
        self.devButton.place(relx=0.1, rely=0.035, anchor='w')

        #main dps label
        self.dpsLabel = Label(self.frame1, text=f'dps: {self.dps: .2f}')
        self.dpsLabel.place(relx=0.75, rely=0.035, anchor='center')

    def clicker(self):
        self.money += 1
        self.update_money_display()

    def devfunc(self):
        self.money += 10000
        self.update_money_display()

    def update_money_display(self):
        self.moneyLabel.config(text=f'Net Worth: ${self.money: .2f}')

    def buy_gatherers(self):
        if self.money >= self.gatherersPrice:
            self.gatherers += 1
            self.money -= self.gatherersPrice
            self.gatherersPrice = round(10 + (1.20) ** self.gatherers, 2)
            self.update_money_display()
            self.gatherersLabel.configure(text=f'{self.gatherers} gatherers')
            self.gatherersPLabel.configure(text=f'${self.gatherersPrice}')

    def buy_miners(self):
        if self.money >= self.minersPrice:
            self.miners += 1
            self.money -= self.minersPrice
            self.minersPrice = round(50 + (1.22) ** self.miners, 2)
            self.update_money_display()
            self.minersLabel.configure(text=f'{self.miners} miners')
            self.minersPLabel.configure(text=f'${self.minersPrice}')

    def buy_refiners(self):
        if self.money >= self.refinersPrice:
            self.refiners += 1
            self.money -= self.refinersPrice
            self.refinersPrice = round(100 + (1.24) ** self.refiners, 2)
            self.update_money_display()
            self.refiners.configure(text=f'{self.miners} miners')
            self.refinersPLabel.configure(text=f'${self.minersPrice}')

    def create_frame2(self):
        self.mbRLabel = Label(self.frame2, text='Medium Backpack ($100): \n Increase gatherers production \n value by 15%')
        self.mbRLabel.place(relx=0.10, rely=0.10, anchor='w')
        self.mbButton = Button(self.frame2, text='Research', command=self.medium_backpack_buy, state=DISABLED)
        self.mbButton.place(relx=0.85, rely=0.10, anchor='e')

    def medium_backpack_buy(self):
        if self.money >= 100:
            self.money -= 100
            self.mbresearch += 1
            self.update_money_display()
            self.update_buttons()

    def create_frame3(self):
        self.fireLabel = Label(self.frame3, text='Fire (10 gatherers): \n Unlocks Refiners   \n Increase gatherers production rate by 20%')
        self.fireLabel.place(relx=0.10, rely=0.10, anchor='w')

        self.firesprite = Image.open('sprites\\sprite_3.png')
        self.firesprite = ImageTk.PhotoImage(self.firesprite)
        self.fireButton = Button(self.frame3, image=self.firesprite, command=self.discoverfire, state=DISABLED)
        self.fireButton.place(relx=0.8, rely=0.10, anchor='e')

    def discoverfire(self):
        if self.gatherers >= 10:
            self.firediscovery += 1

        self.refinersLabel = Label(self.frame1, text=f'{self.refiners} refiners')
        self.refinersLabel.place(relx=0.1, rely=0.3, anchor='w')

        self.refinersPLabel = Label(self.frame1, text=f'${self.refinersPrice}')
        self.refinersPLabel.place(relx=0.3, rely=0.3, anchor='w')

        self.refinersDPSLabel = Label(self.frame1, text='Generates 5dps')
        self.refinersDPSLabel.place(relx=0.8, rely=0.3, anchor='center')

        self.refinerssprite = Image.open('sprites\\sprite_2.png')
        self.refinerssprite = ImageTk.PhotoImage(self.refinerssprite)

        self.refinersButton = Button(self.frame1, image=self.refinerssprite, command=self.buy_refiners, state=DISABLED)
        self.refinersButton.place(relx=0.5, rely=0.3, anchor='center')
    
    def update_money_generation(self):
        if self.gatherers and self.mbresearch >= 1:
            self.money += 1.15*self.gatherers
        else:
            self.money += self.gatherers
        self.money += 2.5*self.miners
        self.money += 5*self.refiners

        self.update_money_display()
        self.after(self.gathererstickspeed, self.update_money_generation)

    def gatherers_tick_speed(self):
        if self.firediscovery == 1:
            self.gathererstickspeed = 1000*0.8

    def update_dps(self):
        self.gathererdps = self.gatherers + 0.15*self.gatherers*self.mbresearch + 0.2*self.gatherers*self.firediscovery
        self.minersdps = 2.5*self.miners
        self.dps = round(self.gathererdps, 2) + round(self.minersdps, 2)
        self.dpsLabel.config(text=f'dps: {self.dps}')
        self.after(1000, self.update_dps)

    def update_buttons(self):
        if self.money >= self.gatherersPrice:
            self.gatherersButton.config(state=ACTIVE)
        else:
            self.gatherersButton.config(state=DISABLED)

        if self.money >= self.minersPrice:
            self.minersButton.config(state=ACTIVE)
        else:
            self.minersButton.config(state=DISABLED)

        if self.money >= 100 and self.gatherers >= 1:
            self.mbButton.config(state=ACTIVE)
        else:
            self.mbButton.config(state=DISABLED)

        if self.mbresearch == 1:
            self.mbButton.config(state=DISABLED)

        if self.gatherers >= 10:
            self.fireButton.config(state=ACTIVE)
        else:
            self.fireButton.config(state=DISABLED)

        if self.firediscovery == 1:
            self.fireButton.config(state=DISABLED)

        self.after(100, self.update_buttons)

if __name__ == '__main__':
    app = CivCremental()
    app.mainloop()