from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a question bank list from the dictionary at data.py
question_bank = []
for question in question_data:
    question_text = question["text"]  # Take text from dictionary
    question_answer = question["answer"]  # Take answer from dictionary
    new_question = Question(question_text, question_answer)  # Create an object for each question
    question_bank.append(new_question)  # Add object to the list

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

score = quiz.score  # final score
print("Quiz completed!")
print(f"Your final score is {score}/{len(quiz.questions_list)}")
