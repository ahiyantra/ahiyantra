#!/bin/bash

<< 'MULTILINE-COMMENT'

Skip to Content
Learn Git


Avatar
Learn Git: ASCII PortfolioBrief
Objective
LEARN GIT
ASCII Portfolio
ASCII art is art made from only the letters, numbers and symbols you can type on your keyboard.

In this project, you’ll use Git backtracking commands to undo mistakes made to an ASCII art portfolio!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
0/11 Complete
Mark the tasks as complete by checking them off
ASCII Portfolio
1.
The ASCII face in portrait.txt had a goatee in the last commit, but it was deleted in the working directory. Taking a second look, you want the goatee back.

Discard changes in the working directory for portrait.txt.

Close and reopen portrait.txt to see the result.

2.
That’s much better! Now, give your portrait some eyebrows. It’s up to you how to do it. One way is to use a few = symbols on the line above the eyes, like this:

  ===       ===
  O           O 
Click Save.

3.
Add the file to the staging area.

4.
Make a commit.

5.
It looks like every file has its date written incorrectly.

Change the completion dates on every file, clicking Save after each change.

6.
Next, add all your changes to the staging area with a single command.

7.
Make a commit.

8.
You forgot to add your “artist name” to each file. Under the date, include the name:

L. Da Vinci
Or whatever name you’d like. Click Save after each file change.

9.
If you know you want to add every file in the working directory to the staging area, instead of adding each file individually, you can use a shortcut:

git add .
The . means “all files”. Adding files to the staging area with . is faster than specifying each file individually, but it’s easy to accidentally add files you don’t want there. Make sure you always know what you’re adding.

10.
It turns out that house.txt is an experiment and doesn’t belong in the commit you’re staging. Reset the staging area to remove house.txt.

11.
Now make a commit.

Code Editor
1234567891011121314151617


Terminal


ASCII Portfolio
0/11 Complete

MULTILINE-COMMENT

echo "xyz"

<< 'MULTILINE-COMMENT'

MULTILINE-COMMENT
