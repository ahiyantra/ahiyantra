#!/bin/bash

<< 'MULTILINE-COMMENT'

Skip to Content


Avatar
Introduction to Cybersecurity: Encryption ProjectBrief
Objective
INTRODUCTION TO CYBERSECURITY
Encryption Project
You are a spy embedded in Evil Corp, an organization determined to carry out nefarious deeds. You’ve intercepted a series of letters. If you can figure out what the messages say, maybe you can stop whatever their secret plan is in time!

This project will require you to use some simple terminal commands to decrypt and translate the messages.

Tasks
7/7 Complete
Mark the tasks as complete by checking them off
Using the Terminal and reading what we can
1.
You’re in! Let’s take a look at what’s in this folder open in the terminal right now. It’s supposed to have the letters you intercepted.

In order to see a list of files in your current directory, type this command:

$ ls
and hit Enter or return key. You can use this command whenever you want to see the files in the current directory.


Stuck? Get a hint
2.
All right it looks like we have a bunch of letters!

Examine them in order that they’re numbered to see if any of them are readable.

In order to output a file’s content in the terminal, type cat followed by the name of the file you want to read, then hit Enter.

To read letter 1: you would type:

$ cat letter_1.txt
and hit Enter or return key.

To clear the screen to make more room, use the

$ clear
command.

When you have examined letters 1-3 stored in .txt files, move on.


Stuck? Get a hint
Decryption
3.
It seems like letter 1 contains a clue that we can use to read letter 2. Something about base64, which is a type of encoding that transforms text into a form that is easier for computers to read and store.

We might not actually need to decipher letter 2 with a key. Let’s try the built-in base64 command.

base64 -d letter_2.txt
The -d stands for decode, by the way.

Oops! We also need the cat command here to grab the contents of the file. Enter this command now:

cat letter_2.txt | base64 -d
Did it do the trick?


Stuck? Get a hint
4.
Excellent work on Letter 2! Letter 3 wasn’t readable at first, but now we know that we need to decrypt it using the Caesar Cipher with a key of 15.

In order to decrypt the Caesar Cipher in letter 3, you will need to use the tr command. tr “rotates” each letter by a certain amount. For example:

$ tr "K-ZA-Jk-za-j" "A-Za-z" 
will rotate each letter 10 spots backwards, because K is 10 letters away from A, and j indicates that it’s rotated backwards. The other parts of the command mean to apply it to all uppercase and lowercase letters from a to z.

To decrypt with a key of 11 would be:

$ tr "L-ZA-Kl-za-k" "A-Za-z
We also need to use the cat command to read the file content first, followed by the | key, so the complete command to decrypt a Caesar Cipher in a file with a key of 10 would be:

cat letter_3.txt | tr "K-ZA-Jk-za-j" "A-Za-z"
Try to come up with the correct command for a key of 15. If you need help, take a look at the hint!


Stuck? Get a hint
5.
All right! After decrypting the Caesar cipher in letter 3, we have the password to the letter 4 zip file! Let’s go ahead and see what’s inside.

Zip files not only compress large files but are also a form of encryption that allows you to put a password on sensitive files.

In order to unzip this file, type unzip followed by the file name

$ unzip letter_3.zip
and then press Enter or return. When you are prompted, enter the password you got from Letter 3. Note that you will not see the password being typed, but if you type in the right password and hit Enter, the file should unzip.

After it’s unzipped, use cat to take a look at the newly available letter_4.txt.

Can you read it now?


Stuck? Get a hint
6.
Excellent work, we are almost there! Reading letter 4 gave us another password we can use to unzip letter 5!

Repeat the unzip and password-entering process for letter 5.

You’ll see what what happened after the password is accepted is that letter_5 is in fact a folder with two files inside!

To see the contents inside, you can use the command:

$ ls letter_5
To read the letter_5.txt, you need to specify that it’s inside the folder letter_5. Run this command:

$ cat letter_5/letter_5.txt
Once you’ve read it, take down this password and move onto the next step!


Stuck? Get a hint
7.
We got yet another password from reading letter 5. There’s also another file called disable_the_lasers.sh in the letter_5 folder.

.sh is a file extension for scripts that run in the terminal. We can run it like this:

$ ./letter_5/disable_the_lasers.sh
and enter the password.

Once you’ve done this… Congratulations! You have saved Kitten-topia! Who would have thought the password to the laser was such a weak password? Looks like Evil Corp. is in need of a good cybersecurity consultant.


Stuck? Get a hint

Terminal

7/7 Complete
Back

MULTILINE-COMMENT

ls
cat letter_1.txt
cat letter_2.txt
cat letter_3.txt
base64 -d letter_2.txt
cat letter_2.txt | base64 -d
cat letter_3.txt | tr "P-ZA-Op-za-o" "A-Za-z"
unzip letter_4.zip
unzip letter_5.zip
ls letter_5
cat letter_5/letter_5.txt
./letter_5/disable_the_lasers.sh

<< 'MULTILINE-COMMENT'

$ ls
letter_1.txt  letter_2.txt  letter_3.txt  letter_4.zip  letter_5.zip
$ cat letter_1.txt
From: Evil Corp.
To: Henchman 71

Dear Henchman,

Welcome to Evil Corp! Your first task will be to destroy 
the planet of Kitten-topia, well known for being inhabited 
almost exclusively by kittens. Here at evil corp we are not 
fond of kittens, and would like you to destroy it. You will 
receive further instructions in subsequent letters. Please 
indicate you received this message with a base64 encoded 
response, to prevent interception. 

Best,

Evil Corp.
$ cat letter_2.txt
RGVhciBFdmlsIENvcnAsCgpUaGFuayB5b3UgZm9yIHlvdXIga2luZCBtZXNzYWdlIG9mIGludHJvZHVjdGlvbiEKSSBhbSBleGNpdGVkIHRvIGJlIGEgcGFydCBvZiB5b3VyIG9yZ2FuaXphdGlvbiBhbmQKdG8gYmVnaW4gYnkgZGVzdHJveWluZyBLaXR0ZW4tdG9waWEuIEkgYW0gYXdhaXRpbmcKeW91ciBmdXJ0aGVyIGluc3RydWN0aW9ucy4gRm9yIGdyZWF0ZXIgc2VjdXJpdHksCnBsZWFzZSBzZW5kIHRoZW0gYXMgYSBDYWVzYXIgQ2lwaGVyIHdpdGggYSBrZXkgb2YKMTUuIExvb2tpbmcgZm9yd2FyZCB0byB5b3VyIGluc3RydWN0aW9ucy4KCkZhaXRoZnVsbHkgeW91cnMsCgpIZW5jaG1hbiA3MSAK
$ cat letter_3.txt
Ugdb: Tkxa Rdge.
Id: Wtcrwbpc 71

Stpg Wtcrwbpc 71,

Iwpcz ndj udg ndjg rdcuxgbpixdc du gtrtxei.
Ndjg xchigjrixdch pgt id sthigdn Zxiitc-idexp
pi 9pb dc Bdcspn qn jhxcv iwt vxpci aphtg qtpb
dc iwt heprt hipixdc. Eatpht qt hjgt id ijgc xi
duu puitglpgs ph xi gtpaan tpih je iwt tatrigxrxin
qxaa. Iwt ephhldgs udg iwt aphtg qtpb lxaa udaadl
xc p htepgpit tbpxa. Lt wpkt id qt rpgtuja ph X
zcdl iwtgt pgt tctbn hexth dc iwt heprt hipixdc
lwd ldjas jht iwxh ephhldgs id sxhpqat iwt aphtg
pcs iwt hpkt Zxiitc-idexp, vxktc iwt deedgijcxin.
Eatpht gthedcs lxiw p ephhldgs egditrits oxe uxat
przcdlatsvxcv gtrtxei du iwxh bthhpvt, ndj rpc
jht iwt ephhldgs: AphtgQtpbhSthigdnZxiitch

Qthi,

Tkxa Rdge.
$ base64 -d letter_2.txt
Dear Evil Corp,

Thank you for your kind message of introduction!
I am excited to be a part of your organization and
to begin by destroying Kitten-topia. I am awaiting
your further instructions. For greater security,
please send them as a Caesar Cipher with a key of
15. Looking forward to your instructions.

Faithfully yours,

Henchman 71 
$ cat letter_2.txt | base64 -d
Dear Evil Corp,

Thank you for your kind message of introduction!
I am excited to be a part of your organization and
to begin by destroying Kitten-topia. I am awaiting
your further instructions. For greater security,
please send them as a Caesar Cipher with a key of
15. Looking forward to your instructions.

Faithfully yours,

Henchman 71 
$ cat letter_3.txt | tr "P-ZA-Op-za-o" "A-Za-z"
From: Evil Corp.
To: Henchman 71

Dear Henchman 71,

Thank you for your confirmation of receipt.
Your instructions are to destroy Kitten-topia
at 9am on Monday by using the giant laser beam
on the space station. Please be sure to turn it
off afterward as it really eats up the electricity
bill. The password for the laser beam will follow
in a separate email. We have to be careful as I
know there are enemy spies on the space station
who would use this password to disable the laser
and the save Kitten-topia, given the opportunity.
Please respond with a password protected zip file
acknowledging receipt of this message, you can
use the password: LaserBeamsDestroyKittens

Best,

Evil Corp.
$ unzip letter_4.zip
Archive:  letter_4.zip
[letter_4.zip] letter_4.txt password: 
password incorrect--reenter: 
  inflating: letter_4.txt            
$ cat letter_4.txt
From: Henchman 71
To: Evil Corp

Dear Evil Corp,

Thank you for your message. I will be 
ready Monday morning. this will be the
first planet I have destroyed so I am 
quite excited. Please send me the 
password for the laser beam. You can 
hide it in a separate zip file and 
make the password:
theyWillNeverCatchUs

Best,

Henchman 71



$ unzip letter_5.zip
Archive:  letter_5.zip
   creating: letter_5/
[letter_5.zip] letter_5/disable_the_lasers.sh password: 
  inflating: letter_5/disable_the_lasers.sh  
  inflating: letter_5/letter_5.txt   
$ ls letter_5
disable_the_lasers.sh  letter_5.txt
$ cat letter_5/letter_5.txt
From: Evil Corp.
To: Henchman 71

Dear Henchman 71,

The password to the laser beam is

Passw0rd!

Make sure that nobody sees this!
The mission is too important to 
compromise, and my experts have
assured me that nobody will be
able to decipher our messages. 

Best,

Evil Corp.


$ ./letter_5/disable_the_lasers.sh
Enter a password to disable the Laser Beam
WRONG PASSWORD
$ ./letter_5/disable_the_lasers.sh
Enter a password to disable the Laser Beam
Disabling lasers!
Kitten-topia is saved!

      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)  


                        _ 
                       | \ 
                       | | 
                       | | 
  |\                   | | 
 /, ~\                / / 
X     |-.....-------./ / 
 ~-. ~  ~              | 
    \             /    | 
     \  /_     ___\   / 
     | /\ ~~~~~   \ | 
     | | \        || | 
     | |\ \       || ) 
    (_/ (_/      ((_/ 
$ 

MULTILINE-COMMENT
