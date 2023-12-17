#!/bin/bash

<< 'MULTILINE-COMMENT'

Skip to Content


Avatar
Learn Git: Manhattan ZooBrief
Objective
LEARN GIT
Manhattan Zoo
Ready to try out some of your new Git knowledge?

In this project, you’ll use Git to keep track of meal guidelines for animals at the Manhattan Zoo.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

Tasks
10/10 Complete
Mark the tasks as complete by checking them off
Manhattan Zoo
1.
Initialize a new Git repository.


Stuck? Get a hint
2.
Check the status of the repository.


Stuck? Get a hint
3.
Add meal-regimens.txt to the staging area.

4.
Make a commit.


Stuck? Get a hint
5.
Include this new info in meal-regimens.txt.

3. Long-Tailed Chinchillas
Meal: 1 bag animal pellets, 1 bag dried fruit, 1/2 bag cashews, 5 carrots, 3 stalks kale
Times: 8:00 am
Directions: disperse contents throughout Chinchilla habitat
Click Save.

6.
Add meal-regimens.txt to the staging area.

7.
Check the status of the Git project.

You should see meal-regimens.txt listed as “modified”.

8.
Make a commit.

9.
View your Git commit history.

If your cursor is stuck in Git log mode, press “q” on your keyboard to escape.


Stuck? Get a hint
10.
Here’s two more animal reports. Include each in meal-regimens.txt, making a new commit for each animal added.

4. Poison Dart Frogs
Meal: 1 bag small crickets
Times: 6:00 am
Directions: empty bag in frog habitat once daily. Do not touch frogs! Extremely poisonous.
 
5. Western Lowland Gorilla
Meal: (Morning) 20 lbs. kale, 10 lbs. celery, 10 lbs. green beans, 5 lbs. carrots, 1 bag sweet potatoes. (Evening) 10 Bananas, 10 apples, 5 oranges, 5 mango, 20 lbs. grapes, 10 lbs. turnips, 5 lbs. white potatoes
Times: 6:30 am, 12:00 pm, 7:00 pm
Directions: feed Gorillas in the morning as group, spread forage items during noon meal, and divide quantities for individual feeding in evening

Code Editor

files
meal-regimens.txt

Code Editor

Terminal


10/10 Complete
Back
Next

MULTILINE-COMMENT

git init
git status
git add meal-regimens.txt
git commit -m "added a file"
git add meal-regimens.txt
git commit -m "edited a file"
git log
ctrl + z
git add meal-regimens.txt
git commit -m "edited a file again"
git add meal-regimens.txt
git commit -m "edited a file once more"
git log
ctrl + z

<< 'MULTILINE-COMMENT'

$ git init
Initialized empty Git repository in /home/ccuser/workspace/manhattan-zoo-1/.git/
$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        meal-regimens.txt

nothing added to commit but untracked files present (use "git add" to track)
$ git add meal-regimens.txt
$ git commit -m "added a file"
[master (root-commit) 19d26d2] added a file
 1 file changed, 14 insertions(+)
 create mode 100644 meal-regimens.txt
$ git add meal-regimens.txt
$ git commit -m "edited a file"
[master 1f109bc] edited a file
 1 file changed, 4 insertions(+)
$ git log
commit 1f109bc7b5cda906325da195f7d35f270aeec000
Author: codecademy <ccuser@codecademy.com>
Date:   Wed Apr 21 15:04:40 2021 +0000

    edited a file

commit 19d26d2bd2e2c274a327a42c322646d1951d7d85
Author: codecademy <ccuser@codecademy.com>
Date:   Wed Apr 21 15:03:56 2021 +0000

    added a file
$ git add meal-regimens.txt
$ git commit -m "edited a file again"
[master dd6bb2b] edited a file again
 1 file changed, 5 insertions(+)
$ git add meal-regimens.txt
$ git commit -m "edited a file once more"
[master 3043b98] edited a file once more
 1 file changed, 5 insertions(+)
$ git log
commit 3043b98e1d32708bfb2f4fda87363927c56c73cf
Author: codecademy <ccuser@codecademy.com>
Date:   Wed Apr 21 15:08:37 2021 +0000

    edited a file once more

commit dd6bb2bed186e87d980fe3c0ec6b6563a3061daa
Author: codecademy <ccuser@codecademy.com>
Date:   Wed Apr 21 15:07:25 2021 +0000

    edited a file again

commit 1f109bc7b5cda906325da195f7d35f270aeec000
Author: codecademy <ccuser@codecademy.com>
Date:   Wed Apr 21 15:04:40 2021 +0000


[1]+  Stopped                 git log
$ 

MULTILINE-COMMENT
