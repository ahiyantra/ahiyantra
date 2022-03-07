atleast = 5;
atmost = 55;

choice = input("Please choose the decimal digit place, above 4 & below 56, upto which you want to find the value of 'pi', followed by pressing the 'enter' key: ");

print("\nYour choice is ❝{}❞!".format(choice));

if choice == "":
  print("\nYou're not allowed to choose nothing. We'll use the default vaue of ❝5❞.");
  choice = atleast;
elif int(atleast) > 555:
  print("\nYou're not allowed to choose this decimal digit place. We'll use the default value of ❝55❞.");
  choice = atmost;
else:
  print("\nYou've chosen the value of ❝{}❞! We'll use it for the calculations!".format(choice));
