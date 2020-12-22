from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("TIC TAC TOE")

clicked = True
count = 0

def disable_all_buttons():
    Button_1.config(state=DISABLED)
    Button_2.config(state=DISABLED)
    Button_3.config(state=DISABLED)
    Button_4.config(state=DISABLED)
    Button_5.config(state=DISABLED)
    Button_6.config(state=DISABLED)
    Button_7.config(state=DISABLED)
    Button_8.config(state=DISABLED)
    Button_9.config(state=DISABLED)

def won():
    global winner
    winner = False
    if Button_1["text"] == "X" and Button_2["text"] == "X" and Button_3["text"] == "X":
        Button_1.config(bg="green")
        Button_2.config(bg="green")
        Button_3.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "X - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_4["text"] == "X" and Button_5["text"] == "X" and Button_6["text"] == "X":
        Button_4.config(bg="green")
        Button_5.config(bg="green")
        Button_6.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "X - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_7["text"] == "X" and Button_8["text"] == "X" and Button_9["text"] == "X":
        Button_7.config(bg="green")
        Button_8.config(bg="green")
        Button_9.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "X - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_1["text"] == "X" and Button_4["text"] == "X" and Button_7["text"] == "X":
        Button_1.config(bg="green")
        Button_4.config(bg="green")
        Button_7.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "X - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_2["text"] == "X" and Button_5["text"] == "X" and Button_8["text"] == "X":
        Button_2.config(bg="green")
        Button_5.config(bg="green")
        Button_8.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "X - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_3["text"] == "X" and Button_6["text"] == "X" and Button_9["text"] == "X":
        Button_3.config(bg="green")
        Button_6.config(bg="green")
        Button_9.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "X - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_1["text"] == "X" and Button_5["text"] == "X" and Button_9["text"] == "X":
        Button_1.config(bg="green")
        Button_5.config(bg="green")
        Button_9.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "X - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_3["text"] == "X" and Button_5["text"] == "X" and Button_7["text"] == "X":
        Button_3.config(bg="green")
        Button_5.config(bg="green")
        Button_7.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "X - HAS WON THE GAME")
        disable_all_buttons()

# To check the rows and columns for the "O"
    if Button_1["text"] == "O" and Button_2["text"] == "O" and Button_3["text"] == "O":
        Button_1.config(bg="green")
        Button_2.config(bg="green")
        Button_3.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "O - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_4["text"] == "O" and Button_5["text"] == "O" and Button_6["text"] == "O":
        Button_4.config(bg="green")
        Button_5.config(bg="green")
        Button_6.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "O - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_7["text"] == "O" and Button_8["text"] == "O" and Button_9["text"] == "O":
        Button_7.config(bg="green")
        Button_8.config(bg="green")
        Button_9.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "O - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_1["text"] == "O" and Button_4["text"] == "O" and Button_7["text"] == "O":
        Button_1.config(bg="green")
        Button_4.config(bg="green")
        Button_7.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "O - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_2["text"] == "O" and Button_5["text"] == "O" and Button_8["text"] == "O":
        Button_2.config(bg="green")
        Button_5.config(bg="green")
        Button_8.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "O - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_3["text"] == "O" and Button_6["text"] == "O" and Button_9["text"] == "O":
        Button_3.config(bg="green")
        Button_6.config(bg="green")
        Button_9.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "O - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_1["text"] == "O" and Button_5["text"] == "O" and Button_9["text"] == "O":
        Button_1.config(bg="green")
        Button_5.config(bg="green")
        Button_9.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "O - HAS WON THE GAME")
        disable_all_buttons()
    elif Button_3["text"] == "O" and Button_5["text"] == "O" and Button_7["text"] == "O":
        Button_3.config(bg="green")
        Button_5.config(bg="green")
        Button_7.config(bg="green")
        winner = True
        messagebox.showinfo("TTT", "O - HAS WON THE GAME")
        disable_all_buttons()

    if count == 9 and winner == False:
        box = Button_1, Button_2, Button_3, Button_4, Button_5, Button_6, Button_7, Button_8, Button_9
        for i in box:
            i.config(bg="lightgreen")
        messagebox.showinfo("TTT", "ITS A TIE\n NO WINNER")
        disable_all_buttons()

def b_clicked(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        won()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        won()
    else:
        messagebox.showerror("TTT", "Sorry already occupied\nChoose another box")

def reset():
    global Button_1, Button_2, Button_3, Button_4, Button_5, Button_6, Button_7, Button_8, Button_9
    global clicked, count
    clicked = True
    count = 0
    Button_1 = Button(root, text = " ", font = ("TimesNewRoman", 30, "bold"), height = 4, width = 8, bg = "SystemButtonFace", command = lambda: b_clicked(Button_1))
    Button_2 = Button(root, text = " ", font = ("TimesNewRoman", 30, "bold"), height = 4, width = 8, bg = "SystemButtonFace", command = lambda: b_clicked(Button_2))
    Button_3 = Button(root, text = " ", font = ("TimesNewRoman", 30, "bold"), height = 4, width = 8, bg = "SystemButtonFace", command = lambda: b_clicked(Button_3))
    Button_4 = Button(root, text = " ", font = ("TimesNewRoman", 30, "bold"), height = 4, width = 8, bg = "SystemButtonFace", command = lambda: b_clicked(Button_4))
    Button_5 = Button(root, text = " ", font = ("TimesNewRoman", 30, "bold"), height = 4, width = 8, bg = "SystemButtonFace", command = lambda: b_clicked(Button_5))
    Button_6 = Button(root, text = " ", font = ("TimesNewRoman", 30, "bold"), height = 4, width = 8, bg = "SystemButtonFace", command = lambda: b_clicked(Button_6))
    Button_7 = Button(root, text = " ", font = ("TimesNewRoman", 30, "bold"), height = 4, width = 8, bg = "SystemButtonFace", command = lambda: b_clicked(Button_7))
    Button_8 = Button(root, text = " ", font = ("TimesNewRoman", 30, "bold"), height = 4, width = 8, bg = "SystemButtonFace", command = lambda: b_clicked(Button_8))
    Button_9 = Button(root, text = " ", font = ("TimesNewRoman", 30, "bold"), height = 4, width = 8, bg = "SystemButtonFace", command = lambda: b_clicked(Button_9))

    Button_1.grid(row = 0, column = 0)
    Button_2.grid(row = 0, column = 1)
    Button_3.grid(row = 0, column = 2)
    Button_4.grid(row = 1, column = 0)
    Button_5.grid(row = 1, column = 1)
    Button_6.grid(row = 1, column = 2)
    Button_7.grid(row = 2, column = 0)
    Button_8.grid(row = 2, column = 1)
    Button_9.grid(row = 2, column = 2)

my_menu = Menu(root)
root.config(menu = my_menu)
options = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="OPTIONS", menu=options)
options.add_command(label="NEW", command=reset)

reset()

root.mainloop()