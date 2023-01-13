import tkinter
import tkinter.messagebox
from tkinter import *
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = password_entry.get()
    if len(password) != 0:
        password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        return tkinter.messagebox.showerror(title="ERROR", message=f"Please fill in the website, username and password entry")

    is_ok = tkinter.messagebox.askokcancel(title=website, message=f"These are the details entered: \nusername: {username}\npassword: {password}\nis it okay to safe?")

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {username} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
pw_manager_window = Tk()
pw_manager_window.title("Password Manager")
pw_manager_window.config(pady=20, padx=20)



myimg = PhotoImage(file="logo.png")

canvas = Canvas()
canvas.config(width=200, height=200, highlightthickness=1)
canvas.create_image(100, 100, image=myimg)
canvas.grid(row=0, column=1)

website_lbl = Label(text="Website:")
website_lbl.grid(row=1, column=0)

username_lbl = Label(text="Email/Username:")
username_lbl.grid(row=2, column=0)

password_lbl = Label(text="Password:")
password_lbl.grid(row=3, column=0)

website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "youremail@provider.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

password_gen_button = Button(text="Generate Password", command=generate_password)
password_gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)


pw_manager_window.mainloop()
