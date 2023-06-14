import random
from tkinter import *

def password_generator():
    pass_entry.delete(0, END)
    lower = 'abcdefghijklmnopqrstuvwxyz'
    higher = lower.upper()
    numbers = "0123456789"
    symbols = "[]{}()*:,._-"
    length = submit()
    length = int(length)
    all = lower + higher + numbers + symbols
    password = "".join(random.sample(all, length))

    return password

def clear():
    entry.delete(0, END)
    pass_entry.delete(0, END)


def submit():
    pass_length = entry.get()
    return pass_length


def generate():
    password1 = password_generator()
    pass_entry.insert(10,password1)

main_window = Tk()
main_window.title("Password generator by Igor")
main_window.geometry("1000x500")

start_label = Label(main_window, text="GUI password generator.", bd=5, font=("Arial", 30, "bold"),
                    pady=20, padx=20, relief=RAISED)
start_label.pack()

controlFrame = Frame(main_window)
controlFrame.pack(side=BOTTOM)

exit_button = Button(controlFrame, text="Exit", bd=3, font=("Times New Roman", 15),
                     padx=5, pady=5, bg="black", command=exit)
exit_button.pack(side=LEFT)

reset_button = Button(controlFrame, text="Reset", bd=3, font=("Times New Roman", 15),
                     padx=5, pady=5, bg="black", command=clear)
reset_button.pack(side=RIGHT)


passFrame = Frame(main_window)
passFrame.pack()

pass_label = Label(passFrame, text="Length of your password:", bd=3, font=("Times New Roman", 30))
pass_label.grid(row=0, column=0)

submit_button = Button(passFrame, text="Submit", bd=3, font=("Times New Roman", 30), command=generate)
submit_button.grid(row=0, column=2)

entry = Entry(passFrame, font= ("Arial", 30), fg="#00FF00")
entry.grid(row=0, column=1)

label3 = Label(passFrame, text= "Your password: ", bd=3, font=("Times New Roman", 30))
label3.grid(row=1, column=0)

pass_entry = Entry(passFrame, font=("Arial", 30, "bold"))

pass_entry.grid(row=1, column=1)


main_window.mainloop()
