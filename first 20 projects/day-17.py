from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
import requests
import json

question_data_link = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean")
question_data =  question_data_link.json()
print(question_data)