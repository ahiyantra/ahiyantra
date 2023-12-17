#!/bin/bash

<< 'MULTILINE-COMMENT'

Skip to Content


Avatar
Learn Git: Birthday PartyBrief
Objective
LEARN GIT
Birthday Party
Let’s practice some Git branching.

In this project, you’ll be using Git to make a 1-page website for your friend Kay’s birthday party.

index.html is written in HTML. Don’’t be afraid! You won’’t be asked to write any HTML from scratch. If you’re interested in learning HTML, check out Codecademy’s HTML/CSS course.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

Tasks
12/12 Complete
Mark the tasks as complete by checking them off
Birthday Party
1.
From the terminal, list the Git branches.

2.
Kay wasn’t sure where she wanted to host the party, so you made several Git branches to explore different locations.

Some of the branches are no longer needed. Delete the following branches:

moma
whitney 
You’ll need the -D option, because these feature branches were never merged into master:

git branch -D branchname
3.
Kay wants to see a version of the webpage that includes an unordered list with bullet points instead of a paragraph to show information about the party.

Create a new branch called unordered-list and switch over to it.

4.
In index.html, replace:

<p>Description: Join Kay in celebrating their 29th birthday with free food and beverages, karaoke and a special appearance by Willy Nelson. Also, feel free to explore the Met museum before or after you stop by! Presents for Kay optional.</p>
with this unordered list:

<ul>
    <li>Join Kay in celebrating their 29th birthday with free food and beverages</li>
    <li>karaoke and a special appearance by Willy Nelson</li>
    <li>explore the Met museum before or after you stop by!</li>
    <li>Birthday presents optional</li>
</ul>
Click Save.

5.
Add index.html to the staging area.

6.
Now make a commit.

7.
Kay approves the changes you made in the unordered-list branch.

Switch over to master. Then, merge unordered-list into master. This will be a fast forward merge.

8.
Kay wants the heading to be way bigger. Create a new branch called big-heading.

9.
Now, switch over the big-heading branch.

To make the heading bigger, replace the line below:

<h1>Kay's Birthday Party</h1>
With this line:

<h1 style="font-size: 72px">Kay's Birthday Party</h1>
Then click Save.

10.
Add index.html to the staging area.

11.
Make a commit.

12.
Kay approves of the giant heading!

Switch back over to the master branch. Then, merge big-heading into master.

Code Editor

123456789101112


Terminal


12/12 Complete
Back

MULTILINE-COMMENT

git branch
git branch -D moma
git branch -D whitney
git branch unordered-list
git checkout unordered-list
git add index.html
git commit -m "replaced paragraph with unordered list"
git checkout master
git merge unordered-list
git branch big-heading
git checkout big-heading
git add index.html
git commit -m "made the heading way bigger"
git checkout master
git merge big-heading

<< 'MULTILINE-COMMENT'

$ git branch
* master
  moma
  whitney
$ git branch -D moma
Deleted branch moma (was 978e5a1).
$ git branch -D whitney
Deleted branch whitney (was 9b384f9).
$ git branch unordered-list
$ git checkout unordered-list
Switched to branch 'unordered-list'
$ git add index.html
$ git commit -m "replaced paragraph with unordered list"
[unordered-list 7f6a226] replaced paragraph with unordered list
 1 file changed, 6 insertions(+), 1 deletion(-)
$ git checkout master
Switched to branch 'master'
$ git merge unordered-list
Updating 1481f5a..7f6a226
Fast-forward
 index.html | 7 ++++++-
 1 file changed, 6 insertions(+), 1 deletion(-)
$ git branch big-heading
$ git checkout big-heading
Switched to branch 'big-heading'
$ git add index.html
$ git commit -m "made the heading way bigger"
[big-heading dacfa3b] made the heading way bigger
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git checkout master
Switched to branch 'master'
$ git merge big-heading
Updating 7f6a226..dacfa3b
Fast-forward
 index.html | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
$ 

MULTILINE-COMMENT
