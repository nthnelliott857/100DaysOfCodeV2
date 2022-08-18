class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions
        self.score = 0
        self.total = len(self.questions_list)

    def still_has_questions(self):
        total_questions = len(self.questions_list)
        return total_questions > self.question_number



    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(response, current_question.answer)
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
