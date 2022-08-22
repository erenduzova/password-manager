from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

entry_mail = Entry(width=35)
entry_mail.grid(row=2, column=1, columnspan=2, sticky="EW")

entry_password = Entry(width=32)
entry_password.grid(row=3, column=1, sticky="W")

# Button's

button_generate = Button(text="Generate Password")
button_generate.grid(row=3, column=2, sticky="EW")

button_add = Button(text="Add", width=36)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
