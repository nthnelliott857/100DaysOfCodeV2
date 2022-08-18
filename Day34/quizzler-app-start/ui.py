from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        # canvas
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # buttons
        no_img = PhotoImage(file=r"images/false.png")
        self.no_button = Button(image=no_img, highlightthickness=0, command=self.statement_is_false)
        self.no_button.grid(column=0, row=2)
        yes_img = PhotoImage(file=r"images/true.png")
        self.yes_button = Button(image=yes_img, highlightthickness=0, command=self.statement_is_true)
        self.yes_button.grid(column=1, row=2)

        # textual elements
        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 20), fg="black")
        self.score_text.grid(column=1, row=0)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=250,
            text="",
            font=("Arial", 15, "italic")
        )

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")
    def statement_is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def statement_is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
            self.window.after(1000)
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
