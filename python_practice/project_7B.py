"""
FLOW, DATA, AND ITERATION
Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00

Premium Ground Shipping

Flat charge: $125.00

Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
7/7Complete
Mark the tasks as complete by checking them off
Finding the Cheapest Shipping Method
1.
First off, we need to know how much it costs to ship a package of given weight by normal ground shipping.

Write a function for the cost of ground shipping. This function should take one parameter, weight, and return the cost of shipping a package of that weight.


Stuck? Get a hint
2.
A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:

8.4\ lb \times \$4.00 + \$20.00 = \$53.608.4 lb×$4.00+$20.00=$53.60
Test that your ground shipping function gets the same value.


Stuck? Get a hint
3.
We’ll also need to make sure we include the price of premium ground shipping in our code.

Create a variable for the cost of premium ground shipping.

Note: this does not need to be a function because the price of premium ground shipping does not change with the weight of the package.

4.
Write a function for the cost of drone shipping. This function should take one parameter, weight, and return the cost of shipping a package of that weight.


Stuck? Get a hint
5.
A package that weighs 1.5 pounds should cost $6.75 to ship by drone:

1.5\ lb \times \$4.50 + \$0.00 = \$6.751.5 lb×$4.50+$0.00=$6.75
Test that your drone shipping function gets the same value.

6.
Using those two functions for ground shipping cost and drone shipping cost, as well as the cost of premium ground shipping, write a function that takes one parameter, weight and prints a statement that tells the user

The shipping method that is cheapest.
How much it would cost to ship a package of said weight using this method.

Stuck? Get a hint
7.
Great job! Now, test your function!

What is the cheapest method of shipping a 4.8 pound package and how much would it cost?

What is the cheapest method of shipping a 41.5 pound package and how much would it cost?

(See hint for answers)


Stuck? Get a hint

Sal's Shipping
7/7Complete
"""

def cgs(weight):
  cost = 0
  if weight < 2:
    cost = weight*1.50 + 20
  elif weight > 2 and weight < 6:
    cost = weight*3.00 + 20
  elif weight > 6 and weight < 10:
    cost = weight*4.00 + 20
  else:
    cost = weight*4.75 + 20
  return cost

print(cgs(8.4))

premium = 125

def pgs(weight):
  return premium

def ds(weight):
  cost = 0
  if weight < 2:
    cost = weight*4.50
  elif weight > 2 and weight < 6:
    cost = weight*9.00
  elif weight > 6 and weight < 10:
    cost = weight*12.00
  else:
    cost = weight*14.25
  return cost

print(ds(1.5))

def cost(weight):
  c1 = cgs(weight)
  c2 = pgs(weight)
  c3 = ds(weight)
  hold = 0
  if c1 < c2 and c1 < c3:
    hold = 1
    print("Ground shipping recommended")
  elif c2 < c1 and c2 < c3:
    hold = 2
    print("Premium ground shipping recommended")
  else:
    hold = 3
    print("Drone shipping recommended")
  if hold == 1:
    print("cost = "+str(c1))
  elif hold == 2:
    print("cost = "+str(c2))
  else:
    print("cost = "+str(c3))
  return ""

print(cost(4.8))

print(cost(41.5))