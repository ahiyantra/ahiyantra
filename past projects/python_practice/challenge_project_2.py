"""

Censor Dispenser

Avatar
Censor DispenserBrief
Objective
Censor Dispenser
Overview
This project is slightly different than others you have encountered thus far on Codecademy. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you’ll be building. There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

Project Goals
You’ve recently gotten a job working in the IT department at one of Silicon Valley’s hottest new startups, AirWeb. The company is developing a state-of-the-art artificial intelligence engine designed to help provide a new perspective on the world’s problems. Interestingly, very few people know the details of AirWeb ‘s work and the company is very secretive about its technology, even to its own investors.

You report directly to the Head of Product, a person named Mr. Cloudy, and he has a very important task for you. You see, every month, the head researchers down in the lab send an email to the board of investors to tell them about the status of the project. Cloudy wants you to intercept these emails and censor any “proprietary information” included in them.

Setup Instructions
If you choose to do this project on your computer instead of Codecademy, you can download what you’ll need by clicking the “Download” button below. If you need help setting up your computer, be sure to check out our setup guides.

Tasks
7/7 Complete
Mark the tasks as complete by checking them off
Prerequisites
1.
In order to complete this project, you should have completed the first 4 milestones of the Codecademy Pro Computer Science Path and the Learn Python: Strings lesson, or completed the first 6 sections of the Learn Python 3 course.

Project Requirements
2.
Write a function that can censor a specific word or phrase from a body of text, and then return the text.

Mr. Cloudy has asked you to use the function to censor all instances of the phrase learning algorithms from the first email, email_one. Mr. Cloudy doesn’t care how you censor it, he just wants it done.

3.
Write a function that can censor not just a specific word or phrase from a body of text, but a whole list of words and phrases, and then return the text.

Mr. Cloudy has asked that you censor all words and phrases from the following list in email_two.

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
4.
The most recent email update has concerned Mr. Cloudy, but not for the reasons you might think. He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the negative language and remove unnecessary instances of ‘negative words.’”

Write a function that can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three.

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

Stuck? Get a hint
5.
This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He tells you, “our company would be ruined! Censor it! Censor it all!”

Write a function that censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words in email_four that come before AND after a term from those two lists.

6.
Great job! The Board of Investors is none the wiser to what is going on in the lab and Mr. Cloudy is very happy.

Take a moment to look over your functions, are they the best they can be? As a challenge, make sure they:

Handle upper and lowercase letters.
Handle punctuation.
Censor words while preserving their length.
Solution
7.
Great work! Visit our forums to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that’s okay! There are multiple ways to solve these projects, and you’ll learn more by seeing others’ code.

Code Editor
12345678910111213141516


Output-only Terminal
Output:
 

Censor Dispenser
7/7 Complete

"""

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read();
email_two = open("email_two.txt", "r").read();
email_three = open("email_three.txt", "r").read();
email_four = open("email_four.txt", "r").read();

def censor_0(body, target):
  sub = "";
  for t in range(0,len(target)):
    if target[t] == " ":
      sub = sub + " ";
    elif target[t] == "_":
      sub = sub + "_";
    elif target[t] == "-":
      sub = sub + "-";
    elif target[t] == "!":
      sub = sub + "!";
    elif target[t] == "?":
      sub = sub + "?";
    elif target[t] == ".":
      sub = sub + ".";
    elif target[t] == ",":
      sub = sub + ",";
    elif target[t] == ";":
      sub = sub + ";";
    elif target[t] == "\'":
      sub = sub + "\'";
    elif target[t] == "\"":
      sub = sub + "\"";
    else:
      sub = sub + "▪";
  
  if (len(target) < 3):
    if (len(target) > 1):
      target0 = " " + target + " ";
      sub0 = " " + sub + " ";
      body = body.replace(target0, sub0);
      body = body.replace(target0.title(), sub0);
      body = body.replace(target0.upper(), sub0);
  else:
    target1 = target + " ";
    sub1 = sub + " ";
    body = body.replace(target1, sub1);
    body = body.replace(target1.title(), sub1);
    body = body.replace(target1.upper(), sub1);
  
  target2 = target + ",";
  sub2 = sub + ",";
  body = body.replace(target2, sub2);
  body = body.replace(target2.title(), sub2);
  body = body.replace(target2.upper(), sub2);
  target3 = target + ".";
  sub3 = sub + ".";
  body = body.replace(target3, sub3);
  body = body.replace(target3.title(), sub3);
  body = body.replace(target3.upper(), sub3);
  target4 = target + ";";
  sub4 = sub + ";";
  body = body.replace(target4, sub4);
  body = body.replace(target4.title(), sub4);
  body = body.replace(target4.upper(), sub4);
  target5 = target + "!";
  sub5 = sub + "!";
  body = body.replace(target5, sub5);
  body = body.replace(target5.title(), sub5);
  body = body.replace(target5.upper(), sub5);
  target6 = target + "?";
  sub6 = sub + "?";
  body = body.replace(target6, sub6);
  body = body.replace(target6.title(), sub6);
  body = body.replace(target6.upper(), sub6);
  target7 = " " + target + "s";
  sub7 = " " + sub + "s";
  body = body.replace(target7, sub7);
  body = body.replace(target7.title(), sub7);
  body = body.replace(target7.upper(), sub7);
  target8 = " " + target + "es";
  sub8 = " " + sub + "es";
  body = body.replace(target8, sub8);
  body = body.replace(target8.title(), sub8);
  body = body.replace(target8.upper(), sub8);
  
  return body;

#print(email_one);

email_one = censor_0(email_one, "learning algorithms");

print("\n e-mail-1\n");

print(email_one);

print("");

def censor_1(body, list0):
  list1 = sorted(list0, key=len, reverse=True)
  #list0.sort(key=len, reverse=True)
  for l in list1:
    body = censor_0(body, l);
  return body;

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"];

#print(email_two);

email_two = censor_1(email_two, proprietary_terms);

print("\n e-mail-2\n");

print(email_two);

print("");

def censor_2(body, list1, list2):
  body1 = censor_1(body, list1);
  body2 = censor_1(body1, list2);
  return body2;

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"];

#print(email_three);

email_three = censor_2(email_three, proprietary_terms, negative_words);

print("\n e-mail-3\n");

print(email_three);

print("");

def censor_3(b0, l1, l2):
  b1 = censor_1(b0, l1);
  b2 = censor_1(b1, l2);
  l3 = b2.split();
  #print(l3);
  l4 = [];
  for v0 in range(0, len(l3)):
    if l3[v0][0]=="▪":
      if ((v0-1)>=0):
        if l3[v0-1][0]!="▪":
          #if l3.count(l3[v0-1]) == 0: #if l4[-1]!=l3[v0-1]:
            l4.append(l3[v0-1]);
      if ((v0+1)<=((len(l3)-1))):
        if l3[v0+1][0]!="▪":
          #if l3.count(l3[v0+1]) == 0: #if l4[-1]!=l3[v0+1]:
            l4.append(l3[v0+1]);
  #print(l4);
  b3 =  censor_1(b2, l4);
  return b3;

email_four = censor_3(email_four, proprietary_terms, negative_words);

print("\n e-mail-4\n");

print(email_four);

print("");
