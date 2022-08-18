import time
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn = {}

try:
    data = pandas.read_csv("Data_Sheet.csv")
    # word_dictionary = {row.spanish_word: row.english_translation for (index, row) in data.iterrows()}
    #words_to_learn = data.to_dict(orient="record")
except FileNotFoundError:
    data = pandas.read_csv("Most Common Spanish Words - Sheet1.csv")
    words_to_learn = data.to_dict(orient="record")
else:
    words_to_learn = data.to_dict(orient="record")



# ---------------------------- get_new_word------------------------------- #
def get_new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(language, text="Spanish", fill="black")
    canvas.itemconfig(meaning, text=current_card["Spanish_Word"], fill="black")
    canvas.itemconfig(flash_card, image=front_image)
    flip_timer = window.after(3000, func=flip_card)
    # window.after(3000)
    # canvas.itemconfig(flash_card, image=back_image)


# ---------------------------- flip_card------------------------------- #
def flip_card():
    global current_card
    canvas.itemconfig(flash_card, image=back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(meaning, text=current_card["English_Translation"], fill="white")
    # window.after(3000, func=flip_card)

# ---------------------------- user_knows_card------------------------------- #
def user_knows_card():
    global current_card, words_to_learn
    words_to_learn.remove(current_card)
    print(f"Length: {len(words_to_learn)}")


# ---------------------------- save------------------------------- #

def save():
    data2 = pandas.DataFrame.from_dict(words_to_learn)
    print(len(data2))
    pandas.DataFrame.to_csv(data2, "Data_Sheet.csv", index=False)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, width=850, height=576)

flip_timer = window.after(3000, func=flip_card)  # window.after has to be stored
# as a variable because we need to call window.after_cancel()

canvas = Canvas(height=500, width=778, highlightthickness=0, bg=BACKGROUND_COLOR)
# canvas = Canvas(height=526, width=800, highlightthickness=0)
front_image = PhotoImage(file=r"images\card_front.png")
back_image = PhotoImage(file=r"images\card_back.png")
# canvas.create_image(400, 263, image=my_image)
flash_card = canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 180, text="", font=("Ariel", 40, "italic"))
meaning = canvas.create_text(400, 280, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

no_image = PhotoImage(file=r"images\wrong.png")
no_button = Button(image=no_image, command=get_new_card)
no_button.grid(row=1, column=0)

yes_image = PhotoImage(file=r"images\right.png")
yes_button = Button(image=yes_image, command=user_knows_card)
yes_button.grid(row=1, column=1)
print(words_to_learn)
get_new_card()
#

window.mainloop()
save()
