"""
DEVELOPMENT SKILLS
Daily Buzz
In this project, you’ll use the commands you just learned to navigate through the files and directories of Daily Buzz, a national newspaper.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
14/14Complete
Mark the tasks as complete by checking them off
1.
Print the working directory.


Stuck? Get a hint
2.
List all files and directories in the current working directory


Stuck? Get a hint
3.
With one command, change directories to the national/politics/ directory.


Stuck? Get a hint
4.
List all files and directories in the working politics/ directory.


Stuck? Get a hint
5.
In the politics/ directory, create a directory called elections/.


Stuck? Get a hint
6.
Change directories into the elections/ directory.


Stuck? Get a hint
7.
In the elections/ directory, make two files candidates.txt and issues.txt


Stuck? Get a hint
8.
Change directories three levels up to the daily-buzz/ directory, and print the working directory.


Stuck? Get a hint
9.
In the daily-buzz/ directory, make a directory called business/ and change directories into the business/ directory.


Stuck? Get a hint
10.
List all files and directories in the business/ directory.


Stuck? Get a hint
11.
From the business/ directory, make a directory called startups/ and change directories into the startups/ directory.


Stuck? Get a hint
12.
Change directories one level up back to the business/ directory.

From the business/ directory, make a directory that is a child of startups/, called disruptors/.


Stuck? Get a hint
13.
From the business/ directory, make three files in the disruptors/ directory. The files should be called tech.txt design.txt and education.txt.


Stuck? Get a hint
14.
Change directories one level up to the daily-buzz/ directory and print the working directory.


Stuck? Get a hint

Daily Buzz
14/14Complete
"""

import os

os.system("pwd")
os.system("ls")
os.system("cd national/politics/")
os.system("ls")
os.system("mkdir elections/")
os.system("cd elections/")
os.system("touch candidates.txt")
os.system("touch issues.txt")
os.system("cd ..")
os.system("cd ..")
os.system("cd ..")
os.system("mkdir business/")
os.system("ls")
os.system("cd business/")
os.system("mkdir startups/")
os.system("cd startups/")
os.system("cd ..")
os.system("mkdir startups/disruptors/")
os.system("touch startups/disruptors/tech.txt")
os.system("touch startups/disruptors/design.txt")
os.system("touch startups/disruptors/education.txt")
os.system("cd ..")
os.system("ls")
