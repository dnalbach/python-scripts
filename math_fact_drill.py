# coding: utf-8
import random
import time
from os import system
import mixpanel
from mixpanel import Mixpanel

mp = Mixpanel("f889f303554b41d71d74f68746438fe0")




# Note that all output string lines are indented 5 spaces on purpose for screen output padding

score = 0
time_limit = 60
start_time = time.time()
time_remaining = True


def get_sign(argument): 
    switcher = { 
        "Addition": "+", 
        "Subtraction": "-", 
        "Multiplication": "x",
        "Division": "÷", 
    }
    return switcher.get(argument, "invalid sign type") 

class MathProblem:
    problem_type_list = ["Addition", "Subtraction", "Multiplication", "Division"]
    first_number = 0
    second_number = 0
    answer = 0
    text = "uninitialized"

    def __init__(self):
        random.seed(time.clock())
        problem_type = random.randint(0, 1)
        if problem_type == 0 :
            self.first_number = random.randint(1, 10)
            self.second_number = random.randint(1, 10)
            self.answer = self.first_number + self.second_number
        elif problem_type == 1 :
            self.first_number = random.randint(10, 20)
            self.second_number = random.randint(1, 10)
            self.answer = self.first_number - self.second_number

        sign = get_sign(self.problem_type_list[problem_type]) 
        self.text = "     %s: \n\n     %s %s %s = " %(self.problem_type_list[problem_type], self.first_number, sign, self.second_number)


system('clear')
user_name = raw_input("\n     What is your first name?  ")
system('clear')

while time_remaining :
    print "\n\n     SCORE: ", score, "\n\n"
    problem = MathProblem()
    print problem.text

    invalid_response = True

    while invalid_response :
        response = raw_input("\n     What is the answer?  ")
    
        try:
            numeric_response = int(response)
            invalid_response = False
        except ValueError:
            print("\n     Your answer was not a valid number. Please try again.")
    
    if numeric_response == problem.answer :
        print "\n     CORRECT"
        score += 1
        time.sleep(.5)
        system('clear')
    else :
        print "\n     WRONG"
        print "\n     The correct answer was: ", problem.answer
        score -= 1
        time.sleep(1)
        system('clear')
    
    # You can also include properties to describe
    # the circumstances of the event
    mp.track(user_name, 'Answer', {
        'problem': problem.text,
        'answer': problem.answer,
        'correct': numeric_response == problem.answer
    })

    current_time = time.time()
    if int(start_time) + time_limit < int(current_time) :
        time_remaining = False
        system('clear')
        print "\n\n     FINAL SCORE: ", score, "\n\n"


    