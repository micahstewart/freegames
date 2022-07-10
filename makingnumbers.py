import random
from turtle import *



def math_problem(user_answer):
    number_one = random.randint(1, 10)
    number_two = random.randint(1, 10)
    answer = str((number_one*number_two))
    problem = ('What is' + ' ' + str(number_one) + ' ' + "times" + ' ' + str(number_two))
    wn = Screen()
    user_answer = wn.textinput(problem,"Enter your answer")
    if user == answer and response > 30:
        wn.bgcolor("blue")
    else:
        textinput(problem, "Wrong! Enter your answer")
    





