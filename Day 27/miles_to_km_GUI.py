from tkinter import *

FONT = ('Arial', 15, 'italic')

def convert_km_mile():
    value_km = float(mile_input.get()) * 1.609
    km.config(text=f"{value_km:.2f}")

window = Tk()
window.title("Mile to km Convert")
window.config(padx=20, pady=20)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

mile_label = Label(text='Miles', font=FONT)
mile_label.grid(column=3, row=0)

equal_label = Label(text='is equal to', font=FONT)
equal_label.grid(column=0, row=1)

km = Label(text='0', font=FONT)
km.grid(column=1, row=1)

km_label = Label(text='Km', font=FONT)
km_label.grid(column=2, row=1)

calculate_button = Button(text='Calculate', command=convert_km_mile)
calculate_button.grid(column=1, row=2)


window.mainloop()