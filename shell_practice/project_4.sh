#!/bin/bash

<< 'MULTILINE-COMMENT'

Skip to Content
Learn the Command Line

Avatar
Learn the Command Line: AtticaBrief
Objective
LEARN THE COMMAND LINE
Attica
Attica, a clothing store, has asked you to help them configure their environment.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
17/17 Complete
Mark the tasks as complete by checking them off
1.
Print the working directory.


Stuck? Get a hint
2.
Create and open a file in nano called hello.txt.


Stuck? Get a hint
3.
Save the string, “Hello, I am nano” in hello.txt.

Save the file, exit nano, and clear the terminal.


Stuck? Get a hint
4.
Use nano to open the bash profile.


Stuck? Get a hint
5.
In the bash profile, add a greeting with the word “Hello” using the echo command. Save the file, exit nano, and clear the terminal.


Stuck? Get a hint
6.
Use the source command to make the greeting available in the current session.

You should see the greeting you created.


Stuck? Get a hint
7.
Open the bash profile, and create two aliases. The first alias should be p for the pwd command and ll for the ls -la command.

Save the file, exit nano, and clear the terminal.


Stuck? Get a hint
8.
Use the source command to make the aliases available in the current session.


Stuck? Get a hint
9.
Test out the aliases you created for the pwd and ls -la command.


Stuck? Get a hint
10.
Open the bash profile and create and export the USER environment variable, setting it equal to your name.

Save the file, exit nano, and clear the terminal.


Stuck? Get a hint
11.
Echo the USER variable.


Stuck? Get a hint
12.
Open the bash profile and create and export the PS1 environment variable, setting it equal to ">> ".

Save the file, exit nano, and clear the terminal.


Stuck? Get a hint
13.
Use the source command to make the prompt available in the current session.


Stuck? Get a hint
14.
Test out the prompt by typing the two aliases you created earlier.


Stuck? Get a hint
15.
Echo the HOME variable.


Stuck? Get a hint
16.
Echo the PATH variable.


Stuck? Get a hint
17.
Return a list of environment variables.


Stuck? Get a hint
Terminal


Attica
17/17 Complete

MULTILINE-COMMENT

pwd
nano hello.txt
"Hello, I am nano"
^o
enter
^x
clear
nano ~/.bash_profile
echo "Hello"
^o
enter
^x
clear
source ~/.bash_profile
nano ~/.bash_profile
alias p="pwd"
alias ll="ls -la"
^o
enter
^x
clear
source ~/.bash_profile
p
ll
nano ~/.bash_profile
export USER="ahi"
^o
enter
^x
clear
echo $USER
nano ~/.bash_profile
export PS1=">> "
^o
enter
^x
clear
source ~/.bash_profile
p
ll
echo $HOME
echo $PATH
env

<< 'MULTILINE-COMMENT'

$ pwd
/home/ccuser/workspace/clothing
$ nano hello.txt
$ clear
$ nano ~/.bash_profile
$ clear
$ source ~/.bash_profile
Hello
$ nano ~/.bash_profile
$ clear
$ source ~/.bash_profile
Hello
$ p
/home/ccuser/workspace/clothing
$ ll
total 4
drwxr-xr-x 2 ccuser ccuser 152 Jan 13 17:26 .
drwxr-xr-x 1 ccuser ccuser  22 Jan 13 17:06 ..
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 dresses.txt
-rw-r--r-- 1 ccuser ccuser  19 Jan 13 17:26 hello.txt
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 jackets.txt
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 pants.txt
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 scarves.txt
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 shirts.txt
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 socks.txt
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 sweaters.txt
$ nano ~/.bash_profile
$ clear
$ echo $USER
ahi
$ nano ~/.bash_profile
$ clear
$ source ~/.bash_profile
Hello
>> p
/home/ccuser/workspace/clothing
>> ll
total 4
drwxr-xr-x 2 ccuser ccuser 152 Jan 13 17:26 .
drwxr-xr-x 1 ccuser ccuser  22 Jan 13 17:06 ..
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 dresses.txt
-rw-r--r-- 1 ccuser ccuser  19 Jan 13 17:26 hello.txt
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 jackets.txt
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 pants.txt
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 scarves.txt
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 shirts.txt
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 socks.txt
-rw-r--r-- 1 ccuser ccuser   0 Jan 13 16:08 sweaters.txt
>> echo $HOME
/home/ccuser
>> echo $PATH
/home/ccuser/.bin:/home/ccuser/node_modules/.bin:/home/ccuser/.gem/ruby/2.3.0/bin:/home/ccuser/.composer/vendor/bin:/home/ccuser/.bin:/home/ccuser/node_modules/.bin:/home/ccuser/.gem/ruby/2.3.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
>> env
HOSTNAME=60e688f199ed
GEM_HOME=/home/ccuser/.gem/ruby/2.3.0
TERM=xterm
USER=ahi
EXPIRES_AT=1610561178
NLTK_DATA=/home/ccuser/.nltk_data
PATH=/home/ccuser/.bin:/home/ccuser/node_modules/.bin:/home/ccuser/.gem/ruby/2.3.0/bin:/home/ccuser/.composer/vendor/bin:/home/ccuser/.bin:/home/ccuser/node_modules/.bin:/home/ccuser/.gem/ruby/2.3.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
CODEX_RUNNER_PATH=/var/codecademy/codex/runners
PWD=/home/ccuser/workspace/clothing
MPLBACKEND=agg
SESSION_ID=5365133b-83dc-4788-9a0e-c108f1c2b3a1
LANG=en_US.UTF-8
TZ=Etc/UTC
PS1=>> 
HOME=/home/ccuser
SHLVL=2
PYTHONPATH=/var/codecademy/runner_contexts/python:
_=/usr/bin/env
>> 

MULTILINE-COMMENT
