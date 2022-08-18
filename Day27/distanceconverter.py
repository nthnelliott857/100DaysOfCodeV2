from tkinter import *

kilometers = 0

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles = Label(text="Text", font=("Arial", 12, "bold"))
# my_label.pack() #this is required for the label to showup
miles.grid(column=2, row=0)
miles.config(text="Miles")

km_label = Label(text="Label", font=("Arial", 12, "bold"))
# my_label.pack() #this is required for the label to showup
km_label.grid(column=2, row=1)
km_label.config(text="Km")

km_value = Label(text="Label", font=("Arial", 12, "bold"))
# my_label.pack() #this is required for the label to showup
km_value.grid(column=1, row=1)
km_value.config(text=0)


is_equal_to = Label(text="Label", font=("Arial", 12, "bold"))
# my_label.pack() #this is required for the label to showup
is_equal_to.grid(column=0, row=1)
is_equal_to.config(text="is equal to")


def calculate():
    new_text = input.get()
    kilometers = float(new_text) * 1.609344
    kilometers = round(kilometers, 2)
    km_value.config(text=str(kilometers))



button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)





window.mainloop()
