"""

Learn Complex Data Structures

Avatar
Learn Complex Data Structures: Choose Your Own Adventure: Wilderness EscapeBrief
Objective
LEARN COMPLEX DATA STRUCTURES
Choose Your Own Adventure: Wilderness Escape
Welcome to Wilderness Escape, an online Choose-Your-Own-Adventure. Our users get a unique story experience by picking the next chapter of their adventure. We use the tree data structure to keep track of the different paths a user may choose. Let’s get started!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
39/39 Complete
Mark the tasks as complete by checking them off
Our Story Begins
1.
This project will be heavily interactive.

To get in the spirit, write a print() function inside of script.py to display “Once upon a time…” in the console.


Stuck? Get a hint
2.
Great! You’ll need to save your changes as you go.

Click “Save”, then, inside of the terminal, enter python3 script.py. This will run the file.

You should see the contents of your print statement in the console.


Stuck? Get a hint
3.
Wonderful! Our application will use the tree data structure to keep track of the different paths a user can choose in their story.

Define a TreeNode class.

4.
Our TreeNode class will keep track of two things:

a portion of the story.
the choices a user can make to progress in the story.
Within TreeNode, define an __init__() method that takes self, story_piece as arguments.


Stuck? Get a hint
5.
Inside of __init__(), assign story_piece to self.story_piece. Also assign self.choices to be an empty Python list.

6.
Our market research indicates users are clamoring for a wilderness tale. Let’s get the story started…

Declare a variable story_root and assign it to an instance of TreeNode with the following text:

"""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
"""

Stuck? Get a hint
7.
Test out that we’re on the right path by printing story_root.story_piece near the bottom of script.py.

In the terminal, run python3 script.py.


Stuck? Get a hint
Taking Input From the User
8.
A Choose-Your-Own-Adventure wouldn’t be any fun if it weren’t interactive. Let’s explore how we can take input from the user. Outside of the TreeNode class, declare a variable user_choice and assign it to input("What is your name? ")


Stuck? Get a hint
9.
Immediately below input(), print out user_choice and click “Save”.

10.
Inside of the terminal type python3 script.py to run our program.

You should see the argument given to input(), “What is your name? “, printed to the screen.

The terminal is waiting for your response. Type in your name and press the enter key.


Stuck? Get a hint
11.
Did you see your name printed out?

This is how users will progress through our Choose-Your-Own-Adventure, they’ll enter a number to select one of the displayed choices.

Experiment a few times typing in different things. Comment out or delete those lines of code so they don’t run and clutter up the terminal.


Stuck? Get a hint
Adding Chapters
12.
Every good story has a beginning, middle, and end. Let’s alter our TreeNode class so we can add the middle and end.

We’ll need an .add_child() method defined within TreeNode that has self and node as parameters.


Stuck? Get a hint
13.
We’re treating each node in the tree as a piece of the story. It’s a Choose-Your-Own-Adventure story, so there are multiple paths the user can take.

Store the argument passed into add_child() inside of self.choices.


Stuck? Get a hint
14.
Let’s add a few more pieces of the story.

Declare choice_a and assign it to a new instance of TreeNode with the following argument:

"""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""
15.
Declare choice_b and assign it to a new instance of TreeNode with the following argument:

"""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""
16.
Call add_child() on story_root and pass choice_a as an argument.


Stuck? Get a hint
17.
Call add_child() on story_root and pass choice_b as an argument.

18.
Wonderful! Now our story has a beginning in the variable story_root, and two choices available for a middle section stored inside of story_root.choices.


Stuck? Get a hint
Our Story So Far
19.
Let’s add some functionality to our TreeNode class so we can move through the story.

Within TreeNode, define .traverse(). It should only take self as an argument.


Stuck? Get a hint
20.
Inside of .traverse(), declare a variable story_node and assign it to self. This variable will track the current portion of the story.

Call print() with story_node.story_piece as an argument.

21.
Test out our .traverse() method by calling it on story_root.

Click “Save” and run our script by typing python3 script.py in the terminal.

You should see the beginning of the story printed out.

22.
We want to take user input and progress through the story as long as there are story choices remaining.

Let’s break it down:

print out the story_node.story_piece.
while story_node.choices has nodes inside…
prompt the user for a choice.
set story_node to be the user’s story choice.
repeat until the story is over!

Stuck? Get a hint
23.
Let’s write out the while loop that will make up the rest of .traverse().

The loop should run as long as story_node.choices is not equivalent to an empty list.

If story_node.choices is an empty list then we know the story is over.


Stuck? Get a hint
24.
Inside of the while loop, declare a variable choice and set it to input() with the argument: "Enter 1 or 2 to continue the story: ".

This is how we will collect the user’s choice for how to progress through the story.


Stuck? Get a hint
25.
Let’s use a conditional to ensure the user is entering valid input.

If choice is not in a list with the valid options, then print out a message asking them to enter a valid choice: 1 or 2.


Stuck? Get a hint
26.
Now let’s write the branch of the conditional where the user has made a valid choice.

We collected input from the terminal, so even if they entered 1, it will be a String data type. Convert it to be an Integer so we can use this choice as an index.

Declare a variable chosen_index and assign it to int() with choice passed as an argument.


Stuck? Get a hint
27.
We’re having our users enter 1 or 2, but the story_node.choices are at index 0 or 1.

Reassign chosen_index to be one less than it was before.

28.
Declare a variable chosen_child and assign it to the appropriate choice from story_node.choices.

Use chosen_index to access the correct element!


Stuck? Get a hint
29.
chosen_child is now our current portion of the story because the user selected this child node.

Use print() to display chosen_child.story_piece.

30.
Finally, set story_node to be chosen_child.

Our while loop will keep checking story_node to see if there are more choices to be made in our story.


Stuck? Get a hint
31.
Congratulations! We have a functioning Choose-Your-Own-Adventure.

At the bottom of script.py, call .traverse() on story_root.

Click “Save”, and run python3 script.py in the terminal.

You should be able to progress through one level of the story!


Stuck? Get a hint
The Final Chapter
32.
Our functionality is all in place, all we have left to do is finish the story. Let’s create the child nodes for choice_a.

Declare a variable choice_a_1 and assign it to an instance of TreeNode with the following string as an argument:

"""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
"""
33.
Declare a variable choice_a_2 and assign it to an instance of TreeNode with the following string as an argument:

"""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.
 
YOU REMAIN LOST.
"""
34.
choice_a_1 and choice_a_2 should be child nodes to choice_a.

Call .add_child() on choice_a to set up the relationship between these nodes.


Stuck? Get a hint
35.
Click “Save” and in the terminal run python3 script.py. Navigate through these new sections of the story.


Stuck? Get a hint
36.
Now let’s create the child nodes for choice_b.

Declare a variable choice_b_1 and assign it to an instance of TreeNode with the following string as an argument:

"""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
 
YOU REMAIN LOST.
"""
37.
Declare a variable choice_b_2 and assign it to an instance of TreeNode with the following string as an argument:

"""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
"""
38.
Set up the appropriate relationship for choice_b_1 and choice_b_2; they should be child nodes of choice_b.

39.
Our story is complete. Click “Save” and run python3 script.py in the terminal.

Have fun navigating through the different branches of the story!

Code Editor
123456789101112131415161718


Terminal


Choose Your Own Adventure: Wilderness Escape
39/39 Complete

"""

######
# TREENODE CLASS
######

class TreeNode:
  print("Once upon a time…")
  user_choice = input("\nWhat is your name? \n")
  print("\n" + str(user_choice).title() + " ... ")
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []
  def add_child(self, node):
    self.choices.append(node)
  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    while len(story_node.choices) > 0:
      choice = input("\nEnter either 1 or 2 to continue the story: \n")
      while int(choice) not in [1, 2]:
        choice = input("\nPlease enter a valid choice: \n")
      chosen_index = int(choice)
      chosen_index -= 1
      chosen_child = story_node.choices[chosen_index]
      print(chosen_child.story_piece)
      story_node = chosen_child

######
# VARIABLES FOR TREE
######

story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left ...
""")

choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.
 
YOU REMAIN LOST.
""")

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

choice_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
 
YOU REMAIN LOST.
""")

choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

######
# TESTING AREA
######

#print(story_root.story_piece)
story_root.traverse()
