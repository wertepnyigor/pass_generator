import random
from tkinter import *
from tkinter import messagebox

def password_generator():
    entry_password.delete(0, END)
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
    length_password.delete(0, END)
    entry_password.delete(0, END)

def submit():
    password_length = length_password.get()
    try:
        if len(password_length) == 0:
            messagebox.showerror(title="Missing Value",
                                 message="Entry box can't be empty, "
                                         "\nmin. legth of password is 1.")
            main_window.focus_set()
            length_password.focus_set()

            return False

        elif int(password_length) > 16:
            messagebox.showwarning(title="Length Error",
                                   message="Password is longer than needed, this program version handle only "
                                            "max. 16 characters.")
            main_window.focus_set()
            length_password.focus_set()

            return False

        elif int(password_length) <= 0:
            messagebox.showerror(title="Length Error",
                                 message="Password length must be longer than 0 characters")

            main_window.focus_set()
            length_password.focus_set()

            return False

        else:
            return password_length

    except ValueError:
            messagebox.showerror(title="Type Error",
                                 message="Length of password can't be a string value, "
                                         "\nplease type correct integer")
            main_window.focus_set()
            length_password.focus_set()

            return False

def generate():
    password1 = password_generator()
    entry_password.insert(1,password1)

main_window = Tk()
main_window.title("Password generator by Igor")
main_window_width = 1000
main_window_height = 500
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

x = int((screen_width/2) - (main_window_width/2))
y = int((screen_height/2) - (main_window_height/2))

main_window.geometry("{}x{}+{}+{}".format(main_window_width, main_window_height, x, y))

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


password_Frame = Frame(main_window)
password_Frame.pack()

label_password = Label(password_Frame, text="Length of your password:", bd=3, font=("Times New Roman", 30))
label_password.grid(row=0, column=0)

submit_button = Button(password_Frame, text="Submit", bd=3, font=("Times New Roman", 30), command=generate)
submit_button.grid(row=0, column=2)

length_password = Entry(password_Frame, font= ("Arial", 30))
length_password.grid(row=0, column=1)
length_password.focus_set()

label3 = Label(password_Frame, text= "Your password: ", bd=3, font=("Times New Roman", 30))
label3.grid(row=1, column=0)

entry_password = Entry(password_Frame, font=("Arial", 30, "bold"))
entry_password.grid(row=1, column=1, sticky='nesw')


main_window.mainloop()
