#Quiz project

from data import question_data
from question_model import Questions

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Questions(question_text, question_answer)
    question_bank.append(new_question)

#TODO asking the questions

que = question_bank.sort()
print(que["text"])

#TODO checking if the answer was correct
#TODO checking if we're the end of the quiz