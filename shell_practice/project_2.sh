#!/bin/bash

<< 'MULTILINE-COMMENT'

Skip to Content
Learn the Command Line

Avatar
Learn the Command Line: ArtusiBrief
Objective
LEARN THE COMMAND LINE
Artusi
Let’s use commands we just learned to manipulate the files and directories of Artusi, an arts supply Store.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
26/26 Complete
Mark the tasks as complete by checking them off
1.
Print the working directory.


Stuck? Get a hint
2.
List all contents in the current directory, including hidden files and directories.


Stuck? Get a hint
3.
List all contents, in long format.


Stuck? Get a hint
4.
List all contents, including hidden files and directories, in long format, ordered by the date and time they were last modified.


Stuck? Get a hint
5.
Change directories to the pencils/ directory. The relative path of the pencils directory is drawing/pencils/.


Stuck? Get a hint
6.
List all contents in the current working directly, including hidden files and directories.


Stuck? Get a hint
7.
Copy the file color.txt to graphite.txt.


Stuck? Get a hint
8.
Change directories into the charcoal/ directory. The relative path to the charcoal directory is ../charcoal/.


Stuck? Get a hint
9.
Copy the file compressed.txt to vine.txt.


Stuck? Get a hint
10.
Copy the file vine.txt to pencils/color.txt. The relative path of the latter is ../pencils/color.txt.


Stuck? Get a hint
11.
From the charcoal/ directory, change directories to the painting/ directory. The relative path is ../../painting/.


Stuck? Get a hint
12.
Print the working directory.


Stuck? Get a hint
13.
List all contents, in long format, including the hidden files and directories, ordered by the date and time they were last modified.


Stuck? Get a hint
14.
Change directories to the brushes/ directory.


Stuck? Get a hint
15.
List all contents, in long format, including the hidden files and directories, ordered by the date and time they were last modified.


Stuck? Get a hint
16.
Copy the files starting with the letter f from the brushes/ directory to the paint/ directory. The path to the paint/ directory is ../paint/.

Without changing directories, list the files and directories of the paint/ directory.


Stuck? Get a hint
17.
Change directories to the sculpting/ directory. The relative path is ../../sculpting/


Stuck? Get a hint
18.
List all contents, in long format, including the hidden files and directories, ordered by the date and time they were last modified.


Stuck? Get a hint
19.
Change directories into the clay/polymer/ directory, and list all contents of the directory.


Stuck? Get a hint
20.
Move airdry.txt into the ceramic/ directory. The relative path to the is ../ceramic/.


Stuck? Get a hint
21.
Change directories into the ceramic/ directory.


Stuck? Get a hint
22.
List all contents, including hidden files and directories.


Stuck? Get a hint
23.
Remove earthenware.txt from the current directory.


Stuck? Get a hint
24.
Change directories one level up back to the clay/ directory.


Stuck? Get a hint
25.
Take a look at the contents of the current directory clay/. Delete the dough/ directory.


Stuck? Get a hint
26.
Change directories two levels up back to the artusi/ directory. Print the working directory.


Stuck? Get a hint
Terminal

Artusi
26/26 Complete

MULTILINE-COMMENT

pwd
ls -a
ls -al
ls -alt
cd drawing/pencils/
ls -a
cp color.txt graphite.txt
cd ../charcoal/
cp compressed.txt vine.txt
cp vine.txt ../pencils/color.txt
cd ../../painting/
pwd
ls -alt
cd brushes/
ls -alt
cp f* ../paint/
ls ../paint/
cd ../../sculpting/
ls -alt
cd clay/polymer/
mv airdry.txt ../ceramic/
cd ../ceramic/
ls -a
rm earthenware.txt
cd ..
ls
rm -r dough/
cd ../..
pwd

<< 'MULTILINE-COMMENT'

$ pwd
/home/ccuser/workspace/artusi
$ ls -a
.  ..  drawing  painting  sculpting
$ ls -al
total 0
drwxr-xr-x 5 ccuser ccuser 54 Mar  5  2016 .
drwxr-xr-x 1 ccuser ccuser 20 Jan  9 18:20 ..
drwxr-xr-x 4 ccuser ccuser 37 Mar  5  2016 drawing
drwxr-xr-x 4 ccuser ccuser 34 Mar  5  2016 painting
drwxr-xr-x 3 ccuser ccuser 18 Mar  5  2016 sculpting
$ ls -alt
total 0
drwxr-xr-x 1 ccuser ccuser 20 Jan  9 18:20 ..
drwxr-xr-x 5 ccuser ccuser 54 Mar  5  2016 .
drwxr-xr-x 4 ccuser ccuser 37 Mar  5  2016 drawing
drwxr-xr-x 4 ccuser ccuser 34 Mar  5  2016 painting
drwxr-xr-x 3 ccuser ccuser 18 Mar  5  2016 sculpting
$ cd drawing/pencils/
$ ls -a
.  ..  color.txt  graphite.txt
$ cp color.txt graphite.txt
$ cd ../charcoal/
$ cp compressed.txt vine.txt
$ cp vine.txt ../pencils/color.txt
$ cd ../../painting/
$ pwd
/home/ccuser/workspace/artusi/painting
$ ls -alt
total 0
drwxr-xr-x 2 ccuser ccuser 69 Jan  9 16:50 brushes
drwxr-xr-x 4 ccuser ccuser 34 Mar  5  2016 .
drwxr-xr-x 5 ccuser ccuser 54 Mar  5  2016 ..
drwxr-xr-x 4 ccuser ccuser 40 Mar  5  2016 paint
$ cd brushes/
$ ls -alt
total 16
drwxr-xr-x 2 ccuser ccuser  69 Jan  9 16:50 .
-rw-r--r-- 1 ccuser ccuser  59 Jan  9 16:50 fan.txt
-rw-r--r-- 1 ccuser ccuser 133 Jan  9 16:50 flat.txt
-rw-r--r-- 1 ccuser ccuser 199 Jan  9 16:50 mop.txt
-rw-r--r-- 1 ccuser ccuser  75 Jan  9 16:50 round.txt
drwxr-xr-x 4 ccuser ccuser  34 Mar  5  2016 ..
$ cp f* ../paint/
$ ls ../paint/
acryllic  fan.txt  flat.txt  watercolor
$ cd ../../sculpting/
$ ls -alt
total 0
drwxr-xr-x 3 ccuser ccuser 18 Mar  5  2016 .
drwxr-xr-x 5 ccuser ccuser 54 Mar  5  2016 ..
drwxr-xr-x 5 ccuser ccuser 49 Mar  5  2016 clay
$ cd clay/polymer/
$ mv airdry.txt ../ceramic/
$ cd ../ceramic/
$ ls -a
.  ..  airdry.txt  earthenware.txt  stoneware.txt
$ rm earthenware.txt
$ cd ..
$ ls
ceramic  dough  polymer
$ rm -r dough/
$ cd ../..
$ pwd
/home/ccuser/workspace/artusi
$ 

MULTILINE-COMMENT
