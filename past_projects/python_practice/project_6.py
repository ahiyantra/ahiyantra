"""
DEVELOPMENT SKILLS
SnapFit Robots, Inc.
Now that you’ve had more practice with the Git workflow, let’s solidify your new skills even more.

In this project, you will be working on assembly instructions for Snap-Fit Robots Inc., a build-it-yourself robot company.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
11/11Complete
Mark the tasks as complete by checking them off
SnapFit Robots Inc.
1.
Initialize a new Git project.

2.
Check the status of the Git project.

You will see multiple files listed in the output as “Untracked”.

3.
Add each file to the Git staging area.

4.
Check the status of the Git project again.

5.
Make a commit.

6.
View your Git commit log.

If your cursor is stuck in Git log mode, press “q” on your keyboard to escape.

7.
Include this line in disclaimer.txt:

Warning: For best battery life, do not leave robot battery charging overnight.
Click Save.

8.
Add the file to the staging area.

9.
Now make a commit.

10.
View your Git commit log again to identify your commit.

11.
Revise each file in whatever ways you’d like. Then add your changes to the staging area and make another commit.


SnapFit Robots, Inc.
11/11Complete
"""

import os

os.system("git init")
os.system("git status")
os.system("git add instructions.txt")
os.system("git add warranty.txt")
os.system("git status")
os.system("git commit")
os.system("git log")
output = open("disclaimer.txt", "a")
output.write("Warning: For best battery life, do not leave robot battery charging overnight.")
output.close()
os.system("git add disclaimer.txt")
os.system("git commit")
os.system("git log")
output = open("instructions.txt", "a")
output.write("Arbitrary revision 1")
output.close()
os.system("git commit")
output = open("warranty.txt", "a")
output.write("Arbitrary revision 1")
output.close()
os.system("git commit")
output = open("disclaimer.txt", "a")
output.write("Arbitrary revision 1")
output.close()
os.system("git commit")
