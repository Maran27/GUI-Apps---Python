from tkinter import *
import random
root = Tk()
root.geometry('400x400')
root.resizable(100, 100)
root.title("Stone Paper Scissors")
root.config(bg = "Pink")
Label(root, text = "Stone, Paper, Scissors", font = "arial 20 bold", bg = "Gray").pack()
user_val = StringVar()
Label(root, text = "Choose AN Option", font = "arial 15 bold", bg = "Yellow").place(x = 15, y = 70)
Label(root, text = "Please enter the first letter in Caps", font = "TimesNewRoman 10", bg = "Lightblue").place(x = 15, y = 105)
Entry(root, font = "arial 15", textvariable = user_val, bg = "Lightgreen").place(x = 90, y = 140)
comp_val = random.randint(1, 3)
if comp_val == 1:
    comp_val = "Stone"
elif comp_val == 2:
    comp_val = "Paper"
else:
    comp_val = "Scissors"
Res = StringVar()
def play():
    user_pick = user_val.get()
    if user_pick == comp_val:
        Res.set("No Point")
    elif user_pick == "Stone" and comp_val == "Paper":
        Res.set("Computer Won -- Computer Selected = Paper")
    elif user_pick == "Stone" and comp_val == "Scissors":
        Res.set("Player Won -- Computer Selected = Scissors")
    elif user_pick == "Paper" and comp_val == "Scissors":
        Res.set("Computer Won -- Computer Selected = Scissors")
    elif user_pick == "Paper" and comp_val == "Stone":
        Res.set("Player Won -- Computer Selected = Stone")
    elif user_pick == "Scissors" and comp_val == "Stone":
        Res.set("Computer Won -- Computer Selected = Stone")
    elif user_pick == "Scissors" and comp_val == "Paper":
        Res.set("Player Won -- Computer Selected = Paper")
    else:
        Res.set("Invalid")
def reset():
    Res.set("")
    user_val.set("")
def exit():
    root.destroy()
Entry(root, font = 'arial 10 bold', textvariable = Res, bg ='antiquewhite2', width = 50,).place(x = 25, y = 250)
Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5, bg ='Green', command = play).place(x = 150, y = 190)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5, bg ='Lightyellow', command = reset).place(x = 70, y = 310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5, bg ='Red', command = exit).place(x=230, y = 310)
root.mainloop()