#!/bin/bash

<< 'MULTILINE-COMMENT'

Skip to Content


Avatar
Learn Git: Ruby Time CalculatorBrief
Objective
LEARN GIT
Ruby Time Calculator
Merge conflicts are challenging even for expert Git users, so it’s good to get as much practice as possible with them.

In this project, you’ll have to resolve merge conflicts in two markdown files. Markdown is a file format that converts easily into HTML. You won’t have to write any markdown, just identify the differences between lines.

Take a deep breath. You can do this!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

Tasks
7/7 Complete
Mark the tasks as complete by checking them off
Ruby Time Calculator
1.
You are currently on master.

Merge the edits branch into the master branch.

This will create two merge conflicts: README.md and examples.md.


Stuck? Get a hint
2.
Using the file navigator, open README.md and examples.md. Identify the merge conflicts.


Stuck? Get a hint
3.
In README.md, keep the file changes from the edits branch. Delete the file changes from HEAD.

Don’t forget to delete all of Git’s special markings that indicate a merge conflict.

Click Save.


Stuck? Get a hint
4.
Add README.md to the staging area.


Stuck? Get a hint
5.
Follow the same order of actions as above for examples.md: keep the edits branch file changes and delete the HEAD changes.

Click Save.


Stuck? Get a hint
6.
Add examples.md to the staging area and make a commit. Your commit message could be “Resolve merge conflict”.


Stuck? Get a hint
7.
Delete the edits branch.


Stuck? Get a hint

Code Editor

files
README.md
examples.md

Code Editor

Terminal


7/7 Complete
Back

MULTILINE-COMMENT

git branch
git merge edits
git add README.md
git add examples.md
git commit -m "resolve merge conflicts"
git branch -d edits

<< 'MULTILINE-COMMENT'

$ git branch
  edits
* master
$ git merge edits
Auto-merging examples.md
CONFLICT (content): Merge conflict in examples.md
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
$ git add README.md
$ git add examples.md
$ git commit -m "resolve merge conflicts"
[master da0f798] resolve merge conflicts
$ git branch -d edits
Deleted branch edits (was 0dc9f6a).
$ 

MULTILINE-COMMENT
