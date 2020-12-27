"""
DEVELOPMENT SKILLS
Bicycle World
Welcome to Bicycle World, the premier text-based bicycle shop! This shop is only accessible to programmers like you, who are familiar with the command line.

In this project, you’ll use the commands you learned to navigate and edit the filesystem of this special shop.

The starting filesystem is shown below. (Bicycle World recently changed owners, who named the main directory bicycle-world-ii.)

bicycle-world-ii
|—— brands.txt
|—— freight/
|   |—— messenger/
|   |—— porteur/
|—— mountain/
|   |—— downhill/
|   |   |—— heavyweight/
|   |   |—— lightweight/
|   |—— hardtail/
|—— racing/
    |—— road/
    |—— track/
If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
16/16Complete
Mark the tasks as complete by checking them off
1.
Print the working directory.

If you ever get lost, you can return to this directory using cd.


Stuck? Get a hint
2.
List the files and directories in the working directory.


Stuck? Get a hint
3.
Change directories to the freight/ directory.


Stuck? Get a hint
4.
List the files and directories in the working directory.


Stuck? Get a hint
5.
Change directories to the porteur/ directory.


Stuck? Get a hint
6.
Change directories up two levels to the bicycle-world-ii/ directory.

List the files and directories in the bicycle-world-ii/ directory.


Stuck? Get a hint
7.
Change directories to the mountain/downhill/ directory.


Stuck? Get a hint
8.
Make a file called dirt.txt.


Stuck? Get a hint
9.
Make a file called mud.txt.


Stuck? Get a hint
10.
List the files and directories in the downhill/ directory.


Stuck? Get a hint
11.
Downhill biking is dangerous: In the downhill/ directory, make a directory called safety/.


Stuck? Get a hint
12.
Change directories to the bicycle-world-ii/ directory.


Stuck? Get a hint
13.
List the contents of the bicycle-world-ii/ directory.


Stuck? Get a hint
14.
The shop is adding a new type of bike!

In bicycle-world-ii/, make a directory called bmx/.


Stuck? Get a hint
15.
Without changing directories from bicycle-world-ii/, make a file in the bmx/ directory called tricks.txt.


Stuck? Get a hint
16.
List all files and directories in the current directory.


Stuck? Get a hint

Bicycle World
16/16Complete
"""

import os

os.system("pwd")
os.system("ls")
os.system("cd freight")
os.system("ls")
os.system("cd porteur")
os.system("cd ..")
os.system("cd ..")
os.system("ls")
os.system("cd mountain/downhill/")
os.system("touch dirt.txt")
os.system("touch mud.txt")
os.system("ls")
os.system("mkdir safety")
os.system("cd ..")
os.system("cd ..")
os.system("ls")
os.system("mkdir bmx")
os.system("touch bmx/tricks.txt")
os.system("ls")
