"""
FLOW, DATA, AND ITERATION
Python Gradebook
You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
7/7Complete
Mark the tasks as complete by checking them off
Create Some Lists:
1.
Create a list called subjects and fill it with the classes you are taking:

"physics"
"calculus"
"poetry"
"history"

Stuck? Get a hint
2.
Create a list called grades and fill it with your scores:

98
97
85
88

Stuck? Get a hint
3.
Use the zip() function to combine subjects and grades.

Save this zip object as a list into a variable called gradebook.


Stuck? Get a hint
4.
Print gradebook.

Does it look how you expected it would?


Stuck? Get a hint
Add More Subjects:
5.
Your grade for Computer Science class just came in! You got a perfect score, 100!

After your definitions of subjects and grades but before you create gradebook, use append to add "computer science" to subjects and 100 to grades.


Stuck? Get a hint
6.
Your grade for visual arts just came in! You got a 93!

After the creation of gradebook (but before you print it out), use append to add ("visual arts", 93) to gradebook.


Stuck? Get a hint
One Big Gradebook!
7.
You also have your grades from last semester, stored in last_semester_gradebook. Create a new variable full_gradebook with the items from both gradebook and last_semester_gradebook.


Stuck? Get a hint

Python Gradebook
7/7Complete
"""

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
subjects.append("computer science")
grades.append(100)
gradebook = list(zip(subjects, grades))
gradebook.append(("visual arts", 93))
print(gradebook)
full_gradebook = gradebook + last_semester_gradebook
