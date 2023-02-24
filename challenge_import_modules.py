#!/usr/bin/env python3
"""CHALLENGE: Import Modules"""

import html
import random

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

#slice
question = trivia["question"]
correct_answer = html.unescape(trivia["correct_answer"])
incorrect_answers = [html.unescape(answer) for answer in trivia["incorrect_answers"]]

# Create a list with all the answers, shuffled
answers = [correct_answer] + incorrect_answers
random.shuffle(answers)

# Render the question and answers in HTML format
print(html.unescape(question))
for answer in answers:
    print(html.unescape(answer))

# Get the user's answer and check if it's correct
user_answer = input("Enter your answer (A, B, C or D): ")
correct_letter = chr(answers.index(correct_answer) + 65)
if user_answer.upper() == correct_letter:
    print("Congratulations! Your answer is correct.")
else:
    print("Sorry, your answer is incorrect. The correct answer is", correct_letter + ".")
