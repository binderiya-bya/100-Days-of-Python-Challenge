There are two files in this lesson: `Day-17-start.py` and `Day-17-the-quiz-project.py`. The `Day-17-start.py` shows the basics of creating class and assigning attributes and functions. 
The quiz runs in `Day-17-the-quiz-project.py`. The question bank is created from `data.py`, which is sourced from a free JSON API at `https://opentdb.com/`. 
`question_model.py` creates a class that takes on the questions and the answers from the database and create two attributes, which is used in creating the question bank. 
The main class `QuizBrain` is written in `quiz_brain.py`. 

## Instructions for the Quiz Project

- Step 1: Create a list of `question` objects with two attributes: `question` and `correct_answer`.
- Step 2: Create a question bank with the `question` objects, created in `Step 1`.
- Step 3: Create a class `QuizBrain` that asks each question from the question bank in order, checks whether the answer is
correct and tracks current score out of number of questions asked, and reports whether the user answers correctly and 
the user's current score.
- Step 4. End the quiz once the question bank runs out of questions and report the final score to the user. 

