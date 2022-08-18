from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label

my_label = Label(text="Label", font=("Arial", 24, "bold"))
#my_label.pack() #this is required for the label to showup
my_label.grid(column=0, row=0)
my_label["text"] = "New Text"
my_label.config(text="New Text")
#button = tkinter.Button()


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
#button.pack()

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# def print_nums(*args):
#     for n in args:
#         print(n)
#
#
# print_nums(1,3,7,9,22)

input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=3, row=2)



















window.mainloop()