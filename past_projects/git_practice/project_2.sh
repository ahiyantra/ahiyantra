#!/bin/bash

<< 'MULTILINE-COMMENT'

Skip to Content


Avatar
Learn Git: SnapFit Robots, Inc.Brief
Objective
LEARN GIT
SnapFit Robots, Inc.
Now that you’ve had more practice with the Git workflow, let’s solidify your new skills even more.

In this project, you will be working on assembly instructions for Snap-Fit Robots Inc., a build-it-yourself robot company.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

Tasks
11/11 Complete
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

Code Editor

files
disclaimer.txt
instructions.txt
warranty.txt

Code Editor

Terminal

11/11 Complete
Back
Next

MULTILINE-COMMENT

git init
git status
git add disclaimer.txt
git add instructions.txt
git add warranty.txt
git status
git commit -m "added three files"
git log
ctrl + z
git add disclaimer.txt
git commit -m "edited a file"
git add .
git commit -m "made random changes to each file"
git log
ctrl + z

<< 'MULTILINE-COMMENT'

$ git init
Initialized empty Git repository in /home/ccuser/workspace/snapfit-robots/.git/
$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        disclaimer.txt
        instructions.txt
        warranty.txt

nothing added to commit but untracked files present (use "git add" to track)
$ git add disclaimer.txt
$ git add instructions.txt
$ git add warranty.txt
$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   disclaimer.txt
        new file:   instructions.txt
        new file:   warranty.txt

$ git commit -m "added three files"
[master (root-commit) df1801e] added three files
 3 files changed, 70 insertions(+)
 create mode 100644 disclaimer.txt
 create mode 100644 instructions.txt
 create mode 100644 warranty.txt
$ git log
commit df1801ef7b557b153cfd402d99a836ad1ac8ae26
Author: codecademy <ccuser@codecademy.com>
Date:   Wed Apr 21 15:13:00 2021 +0000

    added three files
$ git add disclaimer.txt
$ git commit -m "edited a file"
[master 41dddb1] edited a file
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git log
commit 41dddb110463dc90cf1ce0f3dd52a33d3a4b9e2d
Author: codecademy <ccuser@codecademy.com>
Date:   Wed Apr 21 15:16:10 2021 +0000

    edited a file

commit df1801ef7b557b153cfd402d99a836ad1ac8ae26
Author: codecademy <ccuser@codecademy.com>
Date:   Wed Apr 21 15:13:00 2021 +0000

    added three files
$ git add .
$ git commit -m "made random changes to each file"
[master 2b976e8] made random changes to each file
 3 files changed, 5 insertions(+)
$ git log
commit 2b976e8fd739691b0a626880eb2854bc4d4c033f
Author: codecademy <ccuser@codecademy.com>
Date:   Wed Apr 21 15:19:43 2021 +0000

    made random changes to each file

commit 41dddb110463dc90cf1ce0f3dd52a33d3a4b9e2d
Author: codecademy <ccuser@codecademy.com>
Date:   Wed Apr 21 15:16:10 2021 +0000

    edited a file

commit df1801ef7b557b153cfd402d99a836ad1ac8ae26
Author: codecademy <ccuser@codecademy.com>
Date:   Wed Apr 21 15:13:00 2021 +0000


[1]+  Stopped                 git log
$ 

MULTILINE-COMMENT
