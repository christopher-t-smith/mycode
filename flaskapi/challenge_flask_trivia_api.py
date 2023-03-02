#!/usr/bin/env python3
"""CHALLENGE: Flask Trivia API Pt. 2 | Christopher T. Smith"""

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app= Flask(__name__)

# Define a Trivia Question
question = "What color is the sky?"
answer = "blue"

# Define HTML landing Page Route
@app.route("/")
def index():
    return render_template("index.html", questions=question)

# Route for form submission
@app.route("/answer", methods=["POST"])
def answer():
    user_answer = request.form["answer"]

    if user_answer.lower() == answer.lower():
        return redirect("/correct")
    else:
        error_message = "Incorrect. Please try again."
        return render_template("index.html", question=question, error_message=error_message)

# Define route for correct answer page
@app.route("/correct")
def correct():
    return "<h1>Correct Answer!</h1>"

if __name__ == "__main__":
    app.run()
