from tkinter import *
from tkinter import messagebox
import random
import string
import json

FONT = ("Courier", 15, "italic")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = [random.choice(string.ascii_letters) for _ in range(8)]
    symbols = [random.choice(string.punctuation) for _ in range(8)]
    numbers = [str(random.randint(0,9)) for _ in range(8)]

    password = letters + symbols + numbers
    random.shuffle(password)

    return ''.join(password)

def update_password():
    password = generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email" : email,
            "password" : password,
        }
    }

    
    if email in "" or password in "":
        messagebox.showerror(title="Oops", message="Please don't leave ant fields empty!")
    else:
        try:
            with open("Day 30/data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("Day 30/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("Day 30/data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = website_entry.get()

    try:
        with open("Day 30/data.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Website not found", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock = PhotoImage(file="Day 29/logo.png")
canvas.create_image(100, 100, image=padlock)
canvas.grid(column=1, row=0)

website_label = Label(text="Website", font=FONT)
website_label.grid(column=0, row=1)
user_label = Label(text="User/Email", font=FONT)
user_label.grid(column=0, row=2)
password_label = Label(text="Password", font=FONT)
password_label.grid(column=0, row=3)

website_entry = Entry(width=24)
website_entry.grid(column=1,row=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "abc@def.ghi")
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate", command=update_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, columnspan=2, row=4)
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()