from tkinter import *

root = Tk()
root.title("CALCULATOR")
root.config(bg = "black")

my_title = Label(root, text="BASIC CALCULATOR", font="TimesNewRoman 20 bold", bg="white")
my_title.grid(row=0, column=0, columnspan=4, pady=(10, 0))
my_title1 = Label(root, text="Please enter the number", font="TimesNewRoman 10 bold", bg="white")
my_title1.grid(row=1, column=0, columnspan=4, pady=(10, 0))
e = Entry(root, width=50, borderwidth=3, bg="lightgray")
e.grid(row=2, column=0, columnspan=4, padx=15, pady=15)

def button_click(number):
    cur_num = e.get()
    e.delete(0, END)
    e.insert(0, str(cur_num) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    fnum = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(fnum)
    e.delete(0, END)

def button_equal():
    s_num = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(s_num))
    if math == "subtraction":
        e.insert(0, f_num - int(s_num))
    if math == "multiplication":
        e.insert(0, f_num * int(s_num))
    if math == "division":
        e.insert(0, f_num / int(s_num))
    if math == "exponential":
        e.insert(0, f_num ** int(s_num))
    if math == "percentage":
        e.insert(0, f_num / 100)

def button_sub():
    fnum = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(fnum)
    e.delete(0, END)

def button_mul():
    fnum = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(fnum)
    e.delete(0, END)

def button_div():
    fnum = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(fnum)
    e.delete(0, END)

def button_exp():
    fnum = e.get()
    global f_num
    global math
    math = "exponential"
    f_num = int(fnum)
    e.delete(0, END)

def button_per():
    fnum = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = int(fnum)
    e.delete(0, END)

button_1 = Button(root, text=" 1 ", padx=30, pady=15, command=lambda: button_click(1), bg="white")
button_2 = Button(root, text=" 2 ", padx=30, pady=15, command=lambda: button_click(2), bg="white")
button_3 = Button(root, text=" 3 ", padx=30, pady=15, command=lambda: button_click(3), bg="white")
button_4 = Button(root, text=" 4 ", padx=30, pady=15, command=lambda: button_click(4), bg="white")
button_5 = Button(root, text=" 5 ", padx=30, pady=15, command=lambda: button_click(5), bg="white")
button_6 = Button(root, text=" 6 ", padx=30, pady=15, command=lambda: button_click(6), bg="white")
button_7 = Button(root, text=" 7 ", padx=30, pady=15, command=lambda: button_click(7), bg="white")
button_8 = Button(root, text=" 8 ", padx=30, pady=15, command=lambda: button_click(8), bg="white")
button_9 = Button(root, text=" 9 ", padx=30, pady=15, command=lambda: button_click(9), bg="white")
button_0 = Button(root, text=" 0 ", padx=30, pady=15, command=lambda: button_click(0), bg="white")
button_add = Button(root, text=" + ", padx=29, pady=15, command=button_add, bg="lightgreen")
button_exp = Button(root, text=" ^ ", padx=29, pady=15, command=button_exp, bg="lightgreen")
button_per = Button(root, text=" % ", padx=28, pady=15, command=button_per, bg="lightgreen")
button_clear = Button(root, text=" C ", padx=71, pady=15, command=button_clear, bg="orange")
button_equal = Button(root, text=" = ", padx=72, pady=15, command=button_equal, bg="green")
button_sub = Button(root, text=" - ", padx=31, pady=15, command=button_sub, bg="lightgreen")
button_mul = Button(root, text=" * ", padx=31, pady=15, command=button_mul, bg="lightgreen")
button_div = Button(root, text=" / ", padx=31, pady=15, command=button_div, bg="lightgreen")

button_1.grid(row=5, column=2)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=0)
button_4.grid(row=4, column=2)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=0)
button_7.grid(row=3, column=2)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=0)
button_0.grid(row=6, column=0)
button_per.grid(row=6, column=1)
button_clear.grid(row=7, column=0, columnspan=2)
button_add.grid(row=3, column=3)
button_exp.grid(row=6, column=2)
button_equal.grid(row=7, column=2, columnspan=2)
button_sub.grid(row=4, column=3)
button_mul.grid(row=5, column=3)
button_div.grid(row=6, column=3)

root.mainloop()