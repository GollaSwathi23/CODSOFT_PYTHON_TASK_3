from tkinter import *
import random
import string

def Password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "{}?/@!#$%^&*()+_-"
    all_chars = lower + upper + numbers + symbols

    length_value = int(length_var.get())
    password = "".join(random.sample(all_chars, length_value))

    # Update the StringVar associated with the Entry widget
    generated_password_var.set(password)
def accept_password():
    password = generated_password_var.get()
    if password:
        # Here, you can add code to perform actions with the generated password
        # For example, save it to a file or copy it to the clipboard
        print("Accepted password:", password)
        window.destroy()  # Close the tkinter window
    else:
        print("No password generated yet.")
def reset_password():
    generated_password_var.set("")  # Clear the generated password
    length_var.set("")  # Clear the length input field
    user_name_input_area.delete(0, END)          

window = Tk()
window.title('Password')
window.geometry('600x400')
window.configure(bg='azure3')
head = Label(window, text="Password Generator", font=('Sans Serif', 20, 'italic'),bg='mediumpurple', anchor='center', padx=50)
head.pack(fill=X)

user_name = Label(text="Enter Username", font=('times', 15), width=20)
user_name.place(x=60, y=80)
user_name_input_area = Entry(font=('times', 15), width=20)
user_name_input_area.place(x=300, y=80)

length_name = Label(text="Enter Password Length", font=('times', 15), width=20)
length_name.place(x=60, y=120)

# Create StringVar for the password length before using it
length_var = StringVar()

length_field = Entry(font=('times', 15), width=20, textvariable=length_var)
length_field.place(x=300, y=120)

Gen_name = Label(text="Generate Password ", font=('times', 15), width=20)
Gen_name.place(x=60, y=160)

# Create a StringVar to store the generated password
generated_password_var = StringVar()
Gen_name_input_area = Entry(font=('times', 15), width=20, textvariable=generated_password_var)
Gen_name_input_area.place(x=300, y=160)

button = Button(text="Generate",font=(15),width=50, command=Password)
button.place(x=60, y=230)

button_accept = Button(text="Accept", font=(15),width=15,command=accept_password)
button_accept.place(x=80, y=300)

button_reset = Button(text="Reset",font=(15), width=15,command=reset_password)
button_reset.place(x=350, y=300)
window.mainloop()
