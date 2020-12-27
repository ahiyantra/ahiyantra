atleast = 55;
atmost = 555;

choice = input("Choose the decimal digit place (up to 555) upto which you want to find the value of 'pi', followed by pressing the 'enter' key: ");

print("\nYour choice is ❝" + choice + "❞.");

if choice == "":
  print("\nYou're not allowed to choose nothing. We'll use the default vaue of 55.");
  choice = atleast;
elif int(atleast) > 555:
  print("\nYou're not allowed to choose this decimal digit place. We'll use the default value of 555.");
  choice = atmost;
else:
  print("\nYou've chosen the value of " + choice + ". We'll use it.");
