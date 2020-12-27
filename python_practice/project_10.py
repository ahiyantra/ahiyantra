"""
FLOW, DATA, AND ITERATION
Carly's Clippers
You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

You have been provided with three lists:

hairstyles: the names of the cuts offered at Carly’s Clippers
prices: the price of each hairstyle in the hairstyles list
last_week: the number of each hairstyle in hairstyles that was purchased last week
Let’s get started!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
13/13Complete
Mark the tasks as complete by checking them off
Prices and Cuts:
1.
Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.

First, let’s sum up all the prices of haircuts. Create a variable total_price, and set it to 0.


Stuck? Get a hint
2.
Iterate through the prices list and add each price to the variable total_price.


Stuck? Get a hint
3.
After your loop, create a variable called average_price that is the total_price divided by the number of prices.

You can get the number of prices by using the len() function.


Stuck? Get a hint
4.
Print the value of average_price so the output looks like:

Average Haircut Price: <average_price>

Stuck? Get a hint
5.
That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.

Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.


Stuck? Get a hint
6.
Print new_prices.


Stuck? Get a hint
Revenue:
7.
Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

Create a variable called total_revenue and set it to 0.

8.
Use a for loop to create a variable i that goes from 0 to len(hairstyles)

Hint: You can use range() to do this!


Stuck? Get a hint
9.
Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.


Stuck? Get a hint
10.
After your loop, print the value of total_revenue, so the output looks like:

Total Revenue: <total_revenue>
11.
Find the average daily revenue by dividing total_revenue by 7. Call this number average_daily_revenue and print it out.

12.
Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.

You can use range() in your list comprehension to make i go from 0 to len(new_prices) - 1.


Stuck? Get a hint
13.
Print cuts_under_30.

Carly's Clippers
13/13Complete
"""

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price =  0

for p in prices:
  total_price =  total_price + p

average_price = total_price/len(prices)

print("Average Haircut Price: "+str(average_price))

new_prices = [p-5 for p in prices]

print(new_prices)

total_revenue = 0

b = range(len(hairstyles))

i = []

for a in b:
  i = i+[a]

for z in i:
  total_revenue = prices[z] * last_week[z]

print("Total Revenue: "+str(total_revenue))

average_daily_revenue = total_revenue/7

print(average_daily_revenue)

j = range(len(hairstyles))

cuts_under_30 = [hairstyles[i] for i in j if new_prices[i]<30]

print(cuts_under_30)
