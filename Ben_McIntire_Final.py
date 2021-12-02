#  This GUI Program is based off a fake Pizzeria known as Momma Mia's Pizzeria. It will include the sandwhich
#  customization area of their application.
#
#     Variables:
#
#
#

import tkinter as tk
window = tk.Tk()
title = tk.Label(text="Welcome! What would you like to order?")
option1 = tk.Button(text="Chicken N' BBQ", command=addPremade(1))
option2 = tk.Button(text="Pizza Sandwhich", command=addPremade(2))
option3 = tk.Button(text="Chicken Parm", command=addPremade(3))
customButton = tk.Button(text="Click Here to make your own!")

global totalCost
totalCost = 0
def addPremade(cost):
    totalCost += cost
title.pack()
option1.pack()
option2.pack()
option3.pack()
customButton.pack()
tk.mainloop()
