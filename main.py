from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---  ------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_entry = website_input.get()
    email_entry = user_name_input.get()
    password_entry = password_input.get()
    new_data = {
        website_entry: {
            "email": email_entry,
            "password": password_entry,
        }
    }

    if len(website_entry) == 0 or len(password_entry) == 0 or len(email_entry) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty.")

    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- SEARCH DETAILS ------------------------------- #

def find_password():
    website_entry = website_input.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website_entry in data:
                email = data[website_entry]["email"]
                passwords = data[website_entry]["password"]
                messagebox.showinfo(title=website_entry, message=f"Email: {email}\nPassword: {passwords}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_entry} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Label
website = Label(text="Website:")
website.grid(column=0, row=1)

user_name = Label(text="Email/Username:")
user_name.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# Entry
website_input = Entry(width=17)
website_input.grid(column=1, row=1)
website_input.focus()

user_name_input = Entry(width=35)
user_name_input.grid(column=1, row=2, columnspan=2)
user_name_input.insert(0, "nshitikantha@gmail.com")

password_input = Entry(width=17)
password_input.grid(column=1, row=3)

# Button
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
