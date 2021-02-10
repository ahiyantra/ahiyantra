#!/bin/bash

<< 'MULTILINE-COMMENT'

Task Group 1: Navigating the File System
The file structure for this project consists of language files ending in .txt grouped under various sub-directories taking the name of continents. There is a separate sub-directory called todo which also contains language files grouped under continent names.

For example, a top-level view would give you this:

africa/  asia/  europe/  northamerica/  southamerica/  spanish.txt  todo/
A sub-directory view would give you this:

./asia:
arabic.txt  hebrew.txt  hindi.txt  japanese.txt  korean.txt  malay.txt
The todo sub-directory view would appear like this:

./todo:
africa/  asia/  europe/
Task 1
Navigate to the lingua-franca/ project directory in your own file system.

Task 2
Print the working directory.

Task 3
List the content of the current working directory.

Task 4
Make a new directory, world, in the current directory.

Task 5
Create a new file, esperanto.txt in the world directory and list the content of the world directory.

Task Group 2: Viewing and Changing the File System
Task 6
List all the contents of the current working directory based on the following constraints:

content must include hidden files and directories
content must appear in long format
content must be sorted based on the time they were last modified.
Which directory would appear first?

Task 7
List the content of the europe directory. Notice that a file, chinese.txt doesn't belong there. Move that file to the correct directory, asia.

Task 8
List the current working directory. Notice that the file spanish.txt needs to be categorized somewhere. Copy it to the following directories: europe, northamerica, and southamerica. Then remove it from the current directory.

Hint
With the cp command, you can copy multiple files to a single directory but not a single file to multiple directories. Hence, you have to execute the cp command separately for each directory.

Task 9
A directory called todo contains subdirectories of continents with language files in them. List the contents of the directory, todo/*.

Task 10
Please copy these files to their appropriate locations under the current top-level directory.

Hint
All the files under todo/africa/ should be copied to africa. Use the * character as a wildcard to select all files in a directory when you copy them.

Task 11
Then remove all the files and directories of todo/ excluding the todo directory in one step.

Task Group 3: Redirecting Input and Output
Task 12
List all the files in the asia/ directory and save it in a file, asian_language_files.txt in the todo/ directory.

Hint
You can use the ls command along with the > redirect symbol.

Task 13
Instead of writing the contents of a file with a file editor, echo the following statement, Welkom by die Lingua Franca vertaaldienste. into the file afrikaans.txt in the africa directory.

Hint
Use the echo command and the redirect > symbol. For example:

echo "hello" > hello.txt
Task 14
Some of the files in our project which end with the suffix, .txt, have no content in them. List the files, across all the continent directories, that end with .txt that have no content and save the listing in a file, empty_files.txt, in the todo/ directory.

Hint
When a file has no content, there should be a word count of 0! You can use a combination of the wc and grep commands via a pipe | and redirect the final output with the > symbol. Make use of the wildcard * to select all the .txt files from all the directories.

Task 15
Display the content of todo/empty_files.txt to list all the empty files across all the continent directories.

Task 16
The name of our translation service is Lingua Franca, however some of the files mistakenly spell it as Lingua-Franca. Replace the string 'Lingua-Franca' with 'Lingua Franca' in all occurrences in all the .txt files.

Check your work using this command, confirming that there are 0 occurrences of Lingua-Franca across all text files:

grep -Rl 'Lingua-Franca' */*.txt | wc -l
Hint
Use the sed command with the -i option. For example, to replace the typo "hellw" with "hello" in a text file called hello_world.txt, you would use the following command:

sed -i 's/hellw/hello/g' hello_world.txt
Task Group 4: Configuring the Environment
Task 17
Create and open the bash profile with your favorite editor.

Task 18
In the bash profile, add a greeting of your choice. Save the bash profile, exit nano, and clear the terminal window.

Task 19
Source the bash profile to make the greeting available in the current session. You should see the greeting you creating in the above step.

Task 20
Open the bash profile, and create three aliases:

md for the mkdir command
d for date
hy for history
Save the bash profile, exit nano, and clear the terminal window.

Task 21
Source the bash profile to make the aliases available in the current session.

Task 22
Test out the aliases you created for the mkdir, date, and history commands. (Recall that when you test out the alias for mkdir you will need to pass in a directory name as an argument such as translations.) After testing out the mkdir alias, list the directory created.

Task 23
Open the bash profile. Create and export the PS1 environment variable, setting it equal to a prompt of your choice. Be sure to leave a space before the close of the quotations.

Save the bash profile, exit nano, and clear the terminal window.

Task 24
Source the bash profile to make the new prompt available in the current session.

Task 25
Test out the prompt by typing the names of the aliases you created. Remember to list the directory created from the mkdir alias.

Task 26
Last, but not least, return a list of environment variables.

Congratulations on completing this project! You have just completed a series of meaningful commands in your own terminal. The next time you download a project to work on, you can use the command line to easily maneuver between locations, and set up your personal coding environment.

MULTILINE-COMMENT

cd lingua-franca
pwd
ls
mkdir world
touch world/esperanto.txt
ls world
ls -alt
ls europe
mv europe/chinese.txt asia/
ls
cp spanish.txt europe/
cp spanish.txt northamerica/
cp spanish.txt southamerica/
rm spanish.txt
ls todo/*
mv todo/africa/* africa/
mv todo/asia/* asia/
mv todo/europe/* europe/
rm -r todo/*
ls asia/ >> todo/asian_language_files.txt
echo "Welkom by die Lingua Franca vertaaldienste." >> africa/afrikaans.txt
wc -l */*.txt | grep 0 > todo/empty_files.txt
cat todo/empty_files.txt
sed -i 's/Lingua-Franca/Lingua Franca/g' */*.txt
grep -Rl 'Lingua-Franca' */*.txt | wc -l
nano ~/.bash_profile
echo "Greetings! ご挨拶！"
^o
enter
^x
clear
source ~/.bash_profile
nano ~/.bash_profile
alias md="mkdir"
alias d="date"
alias hy="history"
^o
enter
^x
clear
source ~/.bash_profile
md translations
ls
d
hy
clear
nano ~/.bash_profile
export PS1="¥ "
^o
enter
^x
clear
source ~/.bash_profile
md transliterations
ls
d
hy
clear
env

<< 'MULTILINE-COMMENT'

user@user-PC:~/Downloads$ cd lingua-franca
user@user-PC:~/Downloads/lingua-franca$ pwd
/home/user/Downloads/lingua-franca
user@user-PC:~/Downloads/lingua-franca$ ls
africa  europe        solution.html  spanish.txt  todo
asia    northamerica  southamerica   tasks.html
user@user-PC:~/Downloads/lingua-franca$ mkdir world
user@user-PC:~/Downloads/lingua-franca$ touch world/esperanto.txt
user@user-PC:~/Downloads/lingua-franca$ ls world
esperanto.txt
user@user-PC:~/Downloads/lingua-franca$ ls -alt
total 72
drwxrwxr-x 2 user user  4096 Feb  3 19:07 world
drwxrwxr-x 9 user user  4096 Feb  3 18:55 .
drwxr-xr-x 8 user user 12288 Feb  3 18:50 ..
drwxrwxr-x 5 user user  4096 Jan 26 20:34 todo
drwxrwxr-x 2 user user  4096 Jan 26 20:34 northamerica
drwxrwxr-x 2 user user  4096 Jan 26 20:34 southamerica
drwxrwxr-x 2 user user  4096 Jan 26 20:34 europe
drwxrwxr-x 2 user user  4096 Jan 26 20:34 asia
drwxrwxr-x 2 user user  4096 Jan 26 20:34 africa
-rw-rw-r-- 1 user user  9151 Oct  5 14:51 tasks.html
-rw-rw-r-- 1 user user 16043 Oct  5 14:44 solution.html
-rw-rw-r-- 1 user user     0 Sep 22 18:08 spanish.txt
user@user-PC:~/Downloads/lingua-franca$ ls europe
chinese.txt  english.txt  french.txt  german.txt  italian.txt  portuguese.txt  russian.txt
user@user-PC:~/Downloads/lingua-franca$ mv europe/chinese.txt asia/
user@user-PC:~/Downloads/lingua-franca$ ls
africa  asia  europe  northamerica  solution.html  southamerica  spanish.txt  tasks.html  todo  world
user@user-PC:~/Downloads/lingua-franca$ cp spanish.txt europe/
user@user-PC:~/Downloads/lingua-franca$ cp spanish.txt northamerica/
user@user-PC:~/Downloads/lingua-franca$ cp spanish.txt southamerica/
user@user-PC:~/Downloads/lingua-franca$ rm spanish.txt
user@user-PC:~/Downloads/lingua-franca$ ls todo/*
todo/africa:
afrihili.txt

todo/asia:
bengali.txt  punjabi.txt

todo/europe:
yiddish.txt
user@user-PC:~/Downloads/lingua-franca$ mv todo/africa/* africa/
user@user-PC:~/Downloads/lingua-franca$ mv todo/asia/* asia/
user@user-PC:~/Downloads/lingua-franca$ mv todo/europe/* europe/
user@user-PC:~/Downloads/lingua-franca$ rm -r todo/*
user@user-PC:~/Downloads/lingua-franca$ ls asia/ >> todo/asian_language_files.txt
user@user-PC:~/Downloads/lingua-franca$ echo "Welkom by die Lingua Franca vertaaldienste." >> africa/afrikaans.txt
user@user-PC:~/Downloads/lingua-franca$ wc -l */*.txt | grep 0 > todo/empty_files.txt
user@user-PC:~/Downloads/lingua-franca$ cat todo/empty_files.txt
  0 africa/afrihili.txt
  0 asia/bengali.txt
  0 asia/chinese.txt
  0 asia/hebrew.txt
  0 asia/hindi.txt
  0 asia/japanese.txt
  0 asia/punjabi.txt
  0 europe/french.txt
  0 europe/german.txt
  0 europe/italian.txt
  0 europe/russian.txt
  0 europe/spanish.txt
  0 europe/yiddish.txt
  0 northamerica/french.txt
  0 northamerica/spanish.txt
  0 southamerica/spanish.txt
  0 todo/empty_files.txt
  0 world/esperanto.txt
user@user-PC:~/Downloads/lingua-franca$ sed -i 's/Lingua-Franca/Lingua Franca/g' */*.txt
user@user-PC:~/Downloads/lingua-franca$ grep -Rl 'Lingua-Franca' */*.txt | wc -l
0
user@user-PC:~/Downloads/lingua-franca$ nano ~/.bash_profile
user@user-PC:~/Downloads/lingua-franca$ clear
user@user-PC:~/Downloads/lingua-franca$ source ~/.bash_profile
Greetings! ご挨拶！
$ nano ~/.bash_profile
$ clear
$ source ~/.bash_profile
Greetings! ご挨拶！
$ md translations
$ ls
africa  europe        solution.html  tasks.html  translations
asia    northamerica  southamerica   todo        world
$ d
Wed Feb 10 13:37:02 IST 2021
$ hy
 1996  d
 1997  hy
$ clear
$ nano ~/.bash_profile
$ clear
$ source ~/.bash_profile
Greetings! ご挨拶！
¥ md transliterations
¥ ls
africa  europe        solution.html  tasks.html  translations      world
asia    northamerica  southamerica   todo        transliterations
¥ d
Wed Feb 10 13:50:23 IST 2021
¥ hy
 2004  d
 2005  hy
¥ clear
¥ env
¥ 

MULTILINE-COMMENT
