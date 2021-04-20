#!/bin/bash

<< 'MULTILINE-COMMENT'

Skip to Content


Avatar
Learn Git: JavaScript HomeworkBrief
Objective
LEARN GIT
JavaScript Homework
Let’s keep applying the Git collaboration skills we’re learning.

In this project, we’ll be using Git to write comments on your student’s JavaScript homework. Don’t worry! You don’t need to know JavaScript to do the project.

If the code below piques your interest, check out Codecademy’s JavaScript course here.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

Tasks
9/9 Complete
Mark the tasks as complete by checking them off
JavaScript Homework
1.
There is a remote called maryrose-hw which contains your student’s JavaScript homework.

Clone the remote, giving it a name of your choice.

2.
Use the terminal command cd to go into your cloned repository.

cd my_clone
Don’t forget to replace my_clone with the name you gave your clone in the previous step.

3.
Use the file navigator to open homework.js in the code editor.

Be sure to open homework.js in your clone, not in the remote.

4.
From the terminal, create a new branch with Git. Your branch will be commenting on Mary Rose’s JavaScript homework, so name the branch appropriately.

Next, switch over to your new branch.

5.
Time to start commenting on Mary Rose’s JavaScript homework.

Comments are used to leave notes for other programmers or yourself. In JavaScript, you can make a single-line comment by typing // at the beginning of any line. Then type your comment. For example:

// I'm a comment! 
There are a number of comments already in homework.js to guide you.

Make whatever comments you’d like to Mary Rose’s JavaScript homework. Then click Save.

6.
Add your changes to the Git staging area.

7.
Now, make a commit.

8.
Push your branch up to the remote.

9.
Use:

cd ../maryrose-hw
To change directories back to the remote. Use your Git knowledge to see the branch you just pushed.

Code Editor

files
maryrose-hw

Code Editor

Terminal


9/9 Complete
Back

MULTILINE-COMMENT

git clone maryrose-hw mr-hw
cd mr-hw
git branch comments
checkout comments
git add homework.js
git commit -m "commented randomly"
git push origin comments
cd ../maryrose-hw
git branch -a

<< 'MULTILINE-COMMENT'

$ git clone maryrose-hw mr-hw
Cloning into 'mr-hw'...
done.
$ cd mr-hw
$ git branch comments
$ git checkout comments
Switched to branch 'comments'
$ git add homework.js
$ git commit -m "commented randomly"
[comments 22c74e5] commented randomly
 1 file changed, 1 insertion(+)
$ git push origin comments
Counting objects: 3, done.
Delta compression using up to 16 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 289 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To /home/ccuser/workspace/js-homework/maryrose-hw
 * [new branch]      comments -> comments
$ cd ../maryrose-hw
$ git branch -a
  comments
* master
$ 

MULTILINE-COMMENT
