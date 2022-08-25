from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = entry_website.get()
    mail = entry_mail.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": mail,
            "password": password,
        }
    }

    if len(password) <= 0 or len(website) <= 0 or len(mail) <= 0:
        messagebox.showwarning(title="Oops", message="Dont leave any fields empty !")
    else:
        ask_ok = messagebox.askokcancel(title=website, message=f"Email: {mail}\nPassword: {password}\n\n"
                                                               f"Do you want to save ?")
        if ask_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except (FileNotFoundError, json.JSONDecodeError):
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                entry_website.delete(0, 'end')
                entry_password.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Label's
label_website = Label(text="Website :")
label_website.grid(row=1, column=0)

label_mail = Label(text="Email/Username :")
label_mail.grid(row=2, column=0)

label_password = Label(text="Password :")
label_password.grid(row=3, column=0)

# Entries
entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2, sticky="EW")
entry_website.focus()

entry_mail = Entry(width=35)
entry_mail.grid(row=2, column=1, columnspan=2, sticky="EW")

entry_password = Entry(width=32)
entry_password.grid(row=3, column=1, sticky="W")

# Button's

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2, sticky="EW")

button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
