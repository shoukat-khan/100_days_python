from day17_2 import QuestionBank
from day17 import question
from quiz_brain import Question_Brain
list_of_questions = []
for i in QuestionBank:
    list_of_questions.append(question(i["text"], i["answer"]))

quiz = Question_Brain(list_of_questions)

while quiz.still_has_questions():
    quiz.next_question()




 