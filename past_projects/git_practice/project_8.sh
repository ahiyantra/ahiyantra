#!/bin/bash

<< 'MULTILINE-COMMENT'

Skip to Content


Avatar
Learn Git: Recipe BookBrief
Objective
LEARN GIT
Recipe Book
Let’s continue practicing our Git collaboration skills.

In this project, you’ll be playing the role of two collaborators working on a recipe book.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

Tasks
10/10 Complete
Mark the tasks as complete by checking them off
Recipe Book
1.
Go into the veggie-favorites remote by using the cd command:

cd veggie-favorites
2.
Once inside veggie-favorites make a change to chili.txt and/or squash-lasagna.txt in the code editor.

Click Save, add your changes to the Git staging area, and then make a commit.

3.
Go into your clone with:

cd ../veggie-clone
Check out Codecademy’s Command Line course here to learn more about cd ..

4.
Fetch all new work from the remote.

5.
Merge origin/master into your local master branch .

6.
Create a new branch, then switch over to it to work on new-recipe.txt. The recipe can be whatever dish you’d like.

Click Save.

7.
Add your file changes to the staging area and make a commit.

8.
Fetch one more time just for good measure (there won’t be a change).

9.
Push your branch up to the remote.

10.
Navigate back to the remote with:

cd ../veggie-favorites
Confirm the presence of your new Git branch there.

Code Editor

files
veggie-clone
veggie-favorites

Code Editor

Terminal


10/10 Complete
Back

MULTILINE-COMMENT

cd veggie-favorites
git add chili.txt squash-lasagna.txt
git commit -m "altered chili.txt & squash-lasagna.txt" [master 61df069] altered chili.txt & squash-lasagna.txt
cd ../veggie-clone
git fetch
git merge origin/master
git branch new-recipe
git checkout new-recipe
git add new-recipe.txt
git commit -m "altered new-recipe.txt with stir fried vegetables"
git fetch
git push origin new-recipe
cd ../veggie-favorites

<< 'MULTILINE-COMMENT'

$ cd veggie-favorites
$ git add chili.txt squash-lasagna.txt
$ git commit -m "altered chili.txt & squash-lasagna.txt" [master 61df069] altered chili.txt & squash-lasagna.txt
 2 files changed, 3 insertions(+), 1 deletion(-)
$ cd ../veggie-clone
$ git fetch
remote: Counting objects: 13, done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 13 (delta 7), reused 0 (delta 0)
Unpacking objects: 100% (13/13), done.
From /home/ccuser/workspace/recipe-book-a/veggie-favorites
 * [new branch]      master     -> origin/master
$ git merge origin/master
Updating 4681ee4..61df069
Fast-forward
 chili.txt          | 16 +++++++++-------
 margherita.txt     | 11 +++++++----
 squash-lasagna.txt |  3 ++-
 3 files changed, 18 insertions(+), 12 deletions(-)
$ git branch new-recipe
$ git checkout new-recipe
Switched to branch 'new-recipe'
$ git add new-recipe.txt
$ git commit -m "altered new-recipe.txt with stir fried vegetables"
[new-recipe 84ac4c5] altered new-recipe.txt with stir fried vegetables
 1 file changed, 19 insertions(+)
$ git fetch
$ git push origin new-recipe
Counting objects: 3, done.
Delta compression using up to 16 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 669 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To /home/ccuser/workspace/recipe-book-a/veggie-favorites
 * [new branch]      new-recipe -> new-recipe
$ cd ../veggie-favorites
$ 

MULTILINE-COMMENT
