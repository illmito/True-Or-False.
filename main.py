from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    q = questions["question"]
    a = questions["correct_answer"]
    new_question = Question(q, a)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("The quiz has been completed!")
print(f"Final Score: {quiz.score}/{quiz.question_number}")
