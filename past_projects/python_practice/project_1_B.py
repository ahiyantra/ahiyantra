"""
Skip to Content
Python: Hello World

Avatar
Python: Hello World: Receipts for Lovely LoveseatsBrief
Objective
CS 101: INTRODUCTION TO PROGRAMMING
Receipts for Lovely Loveseats
We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.

In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.

Please note: Projects do not run tests against your code. This experience is more open to your interpretation and gives you the freedom to explore. Remember that all variables must be declared before they are referenced in your code.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
20/20 Complete
Mark the tasks as complete by checking them off
Adding In The Catalog
1.
Let’s add in our first item, the Lovely Loveseat that is the store’s namesake. Create a variable called lovely_loveseat_description and assign to it the following string:

Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.

Stuck? Get a hint
2.
Great, now let’s create a price for the loveseat. Create a variable lovely_loveseat_price and set it equal to 254.00.


Stuck? Get a hint
3.
Let’s extend our inventory with another characteristic piece of furniture! Create a variable called stylish_settee_description and assign to it the following string:

Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
4.
Now let’s set the price for our Stylish Settee. Create a variable stylish_settee_price and assign it the value of 180.50.

5.
Fantastic, we just need one more item before we’re ready for business. Create a new variable called luxurious_lamp_description and assign it the following:

Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
6.
Let’s set the price for this item. Create a variable called luxurious_lamp_price and set it equal to 52.15.

7.
In order to be a business, we should also be calculating sales tax. Let’s store that in a variable as well.

Define the variable sales_tax and set it equal to .088. That’s 8.8%.

Our First Customer
8.
Our first customer is making their purchase! Let’s keep a running tally of their expenses by defining a variable called customer_one_total. Since they haven’t purchased anything yet, let’s set that variable equal to 0 for now.

9.
We should also keep a list of the descriptions of things they’re purchasing. Create a variable called customer_one_itemization and set that equal to the empty string "". We’ll tack on the descriptions to this as they make their purchases.


Stuck? Get a hint
10.
Our customer has decided they are going to purchase our Lovely Loveseat! Add the price to customer_one_total.


Stuck? Get a hint
11.
Let’s start keeping track of the items our customer purchased. Add the description of the Lovely Loveseat to customer_one_itemization.


Stuck? Get a hint
12.
Our customer has also decided to purchase the Luxurious Lamp! Let’s add the price to the customer’s total.


Stuck? Get a hint
13.
Let’s keep the itemization up-to-date and add the description of the Luxurious Lamp to our itemization.

14.
They’re ready to check out! Let’s begin by calculating sales tax. Create a variable called customer_one_tax and set it equal to customer_one_total times sales_tax.


Stuck? Get a hint
15.
Add the sales tax to the customer’s total cost.


Stuck? Get a hint
16.
Let’s start printing up their receipt! Begin by printing out the heading for their itemization. Print the phrase "Customer One Items:".


Stuck? Get a hint
17.
Print customer_one_itemization.


Stuck? Get a hint
18.
Now add a heading for their total cost: Print out "Customer One Total:"

19.
Now print out their total! Our first customer now has a receipt for the things they purchased.

20.
Congratulations! We created our catalog and served our first customer. We used our knowledge of strings and numbers to create and update variables. We were able to print out an itemized list and a total cost for our customer. Lovely!

Code Editor
1234567891011


Output-only Terminal
Output:
 

Receipts for Lovely Loveseats
20/20 Complete
"""

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. ";
lovely_loveseat_price = 254.00;
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black. ";
stylish_settee_price = 180.50;
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. ";
luxurious_lamp_price = 52.15;
sales_tax = .088;
customer_one_total = 0;
customer_one_itemization = "";
customer_one_total += lovely_loveseat_price;
customer_one_itemization += lovely_loveseat_description;
customer_one_total += luxurious_lamp_price;
customer_one_itemization += luxurious_lamp_description;
customer_one_tax = customer_one_total * sales_tax;
customer_one_total += customer_one_tax;
print("Customer One Items:");
print(customer_one_itemization);
print("Customer One Total:");
print(customer_one_total);
