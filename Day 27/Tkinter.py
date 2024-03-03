from tkinter import *

def button_clicked():
    my_label.config(text=input.get())

window = Tk()
window.title('My first GUI program')
window.minsize(width=600, height=300)

my_label = Label(text='Label Test', font=('Arial', 30, 'italic'))
my_label.config(text='New Text')
my_label.grid(column=0, row=0)

button = Button(text='Click Me!', command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text='Column 2 Row 0')
new_button.grid(column=2,row=2)

input = Entry()
input.grid(column=3, row=3)



window.mainloop()