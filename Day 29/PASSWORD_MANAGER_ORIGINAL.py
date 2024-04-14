'''THIS IS A ORIGINAL CODE OF PASSWORD MANAGER'''

from tkinter import *
from tkinter import messagebox
import random
import string

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

    
    if email in "" or password in "":
        messagebox.showerror(title="Oops", message="Please don't leave ant fields empty!")
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"These are details entered:\nEmail: {email}"
                f" \nPassword: {password}\nIs okay to save?")
    
    if is_ok == True:
        with open("Day 29/data.txt", 'a') as data:
            data = data.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


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

website_entry = Entry(width=35)
website_entry.grid(column=1, columnspan=2,row=1)
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

window.mainloop()