#!/bin/bash

<< 'MULTILINE-COMMENT'

Skip to Content
Learn the Command Line

Avatar
Learn the Command Line: AthleticaBrief
Objective
LEARN THE COMMAND LINE
Athletica
In this project, you’ll use the commands you just learned to redirect files in Athletica, a sporting events directory.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
15/15 Complete
Mark the tasks as complete by checking them off
1.
Print the working directory.


Stuck? Get a hint
2.
List all files and directories in long format, including hidden files.


Stuck? Get a hint
3.
Use cat to view the contents of basketball.txt.


Stuck? Get a hint
4.
Use cat to view the contents of hockey.txt.


Stuck? Get a hint
5.
Redirect the standard output of basketball.txt into hockey.txt. Then view the contents of hockey.txt.


Stuck? Get a hint
6.
View the contents of lacrosse.txt.


Stuck? Get a hint
7.
Append the contents of lacrosse.txt to the contents of tennis.txt. Then, view the contents of tennis.txt.


Stuck? Get a hint
8.
Redirect the contents of gymnastics.txt as standard input for the cat command.


Stuck? Get a hint
9.
Pipe the standard output of cat lacrosse.txt to the wordcount command.


Stuck? Get a hint
10.
Use cat to view the contents of equipment.txt.


Stuck? Get a hint
11.
Sort the contents of equipment.txt in alphabetical order.


Stuck? Get a hint
12.
Use the uniq command to filter out adjacent, duplicate lines in equipment.txt.


Stuck? Get a hint
13.
Use the grep command to search roster.txt for players from Japan.


Stuck? Get a hint
14.
Use the grep command to search for the string ‘player’ in the current directory (.), and output filenames and lines for matched results.


Stuck? Get a hint
15.
Use cat to view the contents of games.txt. Then, use sed to replace all instances of the word ‘loss’ with ‘win’ in games.txt.


Stuck? Get a hint
Terminal


Athletica
15/15 Complete

MULTILINE-COMMENT

pwd
ls -al
cat basketball.txt
cat hockey.txt
cat basketball.txt > hockey.txt
cat hockey.txt
cat lacrosse.txt
cat lacrosse.txt >> tennis.txt
cat tennis.txt
cat < gymnastics.txt
cat lacrosse.txt | wc
cat equipment.txt
sort equipment.txt
uniq equipment.txt
grep Japan roster.txt
grep -R player .
cat games.txt
sed 's/loss/win/g' games.txt

<< 'MULTILINE-COMMENT'

$ pwd
/home/ccuser/workspace/athletica
$ ls -al
total 56
drwxr-xr-x 2 ccuser ccuser  259 Jan 11 15:36 .
drwxr-xr-x 1 ccuser ccuser   23 Jan 11 17:34 ..
-rw-r--r-- 1 ccuser ccuser  102 Jan 11 15:36 badminton.txt
-rw-r--r-- 1 ccuser ccuser   97 Jan 11 15:36 basketball.txt
-rw-r--r-- 1 ccuser ccuser  161 Jan 11 15:36 cricket.txt
-rw-r--r-- 1 ccuser ccuser 6148 Mar  5  2016 .DS_Store
-rw-r--r-- 1 ccuser ccuser  304 Jan 11 15:36 equipment.txt
-rw-r--r-- 1 ccuser ccuser  117 Jan 11 15:36 football.txt
-rw-r--r-- 1 ccuser ccuser  393 Jan 11 15:36 games.txt
-rw-r--r-- 1 ccuser ccuser  130 Jan 11 15:36 gymnastics.txt
-rw-r--r-- 1 ccuser ccuser   97 Jan 11 17:38 hockey.txt
-rw-r--r-- 1 ccuser ccuser  159 Jan 11 15:36 lacrosse.txt
-rw-r--r-- 1 ccuser ccuser  605 Jan 11 15:36 roster.txt
-rw-r--r-- 1 ccuser ccuser   69 Jan 11 15:36 swimming.txt
-rw-r--r-- 1 ccuser ccuser  319 Jan 11 17:38 tennis.txt
$ cat basketball.txt
Basketball is a sport played by two teams of five players on a rectangular court. Src: Wikipedia
$ cat hockey.txt
Basketball is a sport played by two teams of five players on a rectangular court. Src: Wikipedia
$ cat basketball.txt > hockey.txt
$ cat hockey.txt
Basketball is a sport played by two teams of five players on a rectangular court. Src: Wikipedia
$ cat lacrosse.txt
Lacrosse is a contact team sport played between two teams using a small rubber ball and a long-handled stick called a crosse or lacrosse stick. Src: Wikipedia
$ cat lacrosse.txt >> tennis.txt
$ cat tennis.txt
Tennis is a racket sport that can be played individually against a single opponent (singles) or between two teams of two players each (doubles). Src: Wikipedia
Lacrosse is a contact team sport played between two teams using a small rubber ball and a long-handled stick called a crosse or lacrosse stick. Src: Wikipedia
Lacrosse is a contact team sport played between two teams using a small rubber ball and a long-handled stick called a crosse or lacrosse stick. Src: Wikipedia
$ cat < gymnastics.txt
Gymnastics is a sport involving the performance of exercises requiring strength, flexibility, balance and control. Src: Wikipedia
$ cat lacrosse.txt | wc
      1      27     159
$ cat equipment.txt
baseball
shuttlecock
shuttlecock
helmet
football
cleats
cleats
cleats
tennis ball
baseball bat
lacrosse stick
hockey stick
hockey stick
hockey stick
tennis racket
cricket bat
cricket bat
cricket bat
goggles
googles
swimming cap
lacrosse ball
hockey puck
sneakers
sneakers
skates
skates
skates
shinguards
$ sort equipment.txt
baseball
baseball bat
cleats
cleats
cleats
cricket bat
cricket bat
cricket bat
football
goggles
googles
helmet
hockey puck
hockey stick
hockey stick
hockey stick
lacrosse ball
lacrosse stick
shinguards
shuttlecock
shuttlecock
skates
skates
skates
sneakers
sneakers
swimming cap
tennis ball
tennis racket
$ uniq equipment.txt
baseball
shuttlecock
helmet
football
cleats
tennis ball
baseball bat
lacrosse stick
hockey stick
tennis racket
cricket bat
goggles
googles
swimming cap
lacrosse ball
hockey puck
sneakers
skates
shinguards
$ grep Japan roster.txt
Yuki Hayashi, Swimming: Japan
Misako Sato, Gymnastics: Japan
Takumi Fujiwara, Basketball: Japan
Toshi Ogawa, Badminton: Japan
$ grep -R player .
./basketball.txt:Basketball is a sport played by two teams of five players on a rectangular court. Src: Wikipedia
./cricket.txt:Cricket is a bat-and-ball game played between two teams of 11 players each on a field at the centre of which is a rectangular 22-yard-long pitch. Src: Wikipedia
./hockey.txt:Basketball is a sport played by two teams of five players on a rectangular court. Src: Wikipedia
./tennis.txt:Tennis is a racket sport that can be played individually against a single opponent (singles) or between two teams of two players each (doubles). Src: Wikipedia
$ cat games.txt
Australia vs United Kingdom
Australia: loss

United States vs South Africa
United States: loss

Mexico vs Colombia
Colombia: loss

Brazil vs Argentina
Brazil: loss

Kenya vs Ghana
Kenya: loss

Jordan vs Morocco
Morocco: loss

Malaysia vs Singapore
Singapore: loss

India vs China
India: loss

Pakistan vs Uzbekistan
Uzbekistan: loss

Greece vs Turkey
Greece: loss

France vs Spain
France: loss
$ sed 's/loss/win/g' games.txt
Australia vs United Kingdom
Australia: win

United States vs South Africa
United States: win

Mexico vs Colombia
Colombia: win

Brazil vs Argentina
Brazil: win

Kenya vs Ghana
Kenya: win

Jordan vs Morocco
Morocco: win

Malaysia vs Singapore
Singapore: win

India vs China
India: win

Pakistan vs Uzbekistan
Uzbekistan: win

Greece vs Turkey
Greece: win

France vs Spain
$ 

MULTILINE-COMMENT
