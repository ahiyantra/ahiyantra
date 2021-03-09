"""
Skip to Content
How to Implement Search Algorithms with...


Avatar
How to Implement Search Algorithms with Python: SearchcademyBrief
Objective
HOW TO IMPLEMENT SEARCH ALGORITHMS WITH PYTHON
Searchcademy
In order to test a product, many companies use empty or “fake” data. Our company, Searchcademy, uses empty sparsely sorted data to test its awesome search engine. What exactly does that mean? Sparsely Sorted Data is data such that there is empty data in between the sorted values. For instance, an example dataset might look like:

["Arthur", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth", "", "", "", "Zachary"]
In this project, we will implement a modified version of iterative binary search to search through a sparsely sorted dataset.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
17/17 Complete
Mark the tasks as complete by checking them off
Set Up the Function
1.
Within the function, sparse_search, after the print statements, do the following:

Create two variables, first and last, and set them equal to the first and last positions in the dataset.

Stuck? Get a hint
2.
Next, we will keep iterating until we find our search value.

Create a while loop that checks if first is less than or equal to last.

Check if the Middle is Empty
3.
Within the while loop, create a variable called mid and set it to the average of first and last.

Remember to use // in python3 for integer division.


Stuck? Get a hint
4.
Now, we will check if the middle is empty. If so, we will search surrounding values.

In the while loop, create an if statement that checks the following:

mid of the data is empty

Stuck? Get a hint
5.
Now, we will check the surrounding values.

Within the if statement, do the following:

Create a variable, left, and set it equal to the position directly left of the mid.
Create a variable, right, and set it equal to the position directly right of the mid

Stuck? Get a hint
6.
Within the if statement, create a while(True) loop. In this loop, we will be checking if the surrounding values are empty and will break once we find a non-empty value.

7.
First, we will check if we have iterated through the entire dataset and have not found a non-empty value.

In the new inner while loop, check if both of the following conditions are met:

left is less than first
right is greater than last
If so, do the following:

Print the statement: "{0} is not in the dataset". {0} corresponds to the search_val.
return from the function

Stuck? Get a hint
8.
Save your code. In the terminal, run the following command:

python -c 'import script; script.sparse_search([""], "Hello")'
9.
Now, we will check the value to the right.

In the inner while loop, create an elif statement that checks if both of the following are True:

right is the less than or equal to last
data[right] is not empty.
If so, do the following:

Set mid equal to right
break out of the inner while loop

Stuck? Get a hint
10.
Now, we will check the value to the left.

In the inner while loop, create another elif statement that checks if both of the following are True:

left is greater than or equal to first
data[left] is not empty
If so, do the following:

Set mid equal to left
break out of the inner while loop
11.
If none of the statements are true, then we will move our pointers.

In the inner while loop, after the conditional statements, do the following:

Increment right by 1
Decrement left by 1
Check if the Search Value is Equal to the Middle
12.
Now that we handled the empty data, let’s continue with regular binary search. We will first check if the middle of the data is equal to our search value.

Outside the inner while loop and below its encompassing if statement, check if the following is true:

mid of the data is equal to the search_val
If so, do the following:

Print the statement: "{0} found at position {1}". {0} corresponds to the search_val and {1} corresponds to the mid
return from the function.

Stuck? Get a hint
13.
Save your code. In the terminal run the following commands:

python -c 'import script; script.sparse_search(["A", "", "", "", "B", "", "", "", "C"], "B")'
python -c 'import script; script.sparse_search(["A", "", "", "", ""], "A")'
python -c 'import script; script.sparse_search(["", "", "", "", "Z"], "Z")'
Check if the Search Value is Less Than the Middle
14.
Below the if statement, check if the following is true:

search_val is less than data[mid] If so, do the following:
Set last equal to mid - 1
Check if the Search Value is Greater Than the Middle
15.
Below the if statement, check if the following is true:

search_val is greater than data[mid]
If so, do the following:

Set first equal to mid + 1
Return "Value not in data"
16.
Outside of the outer while loop, do the following:

Print the statement: "{0} is not in the dataset". {0} corresponds to the search_val.
Testing
17.
In order to test your code, try running the following commands in the terminal, or make some commands of your own.

python -c 'import script; script.sparse_search(["A", "", "", "", "B", "", "", "", "C", "", "", "D"], "C")'
python -c 'import script; script.sparse_search(["A", "B", "", "", "E"], "A")'
python -c 'import script; script.sparse_search(["", "X", "", "Y", "Z"], "Z")'
python -c 'import script; script.sparse_search(["A", "", "", "", "B", "", "", "", "C"], "D")'
python -c 'import script; script.sparse_search(["Apple", "", "Banana", "", "", "", "", "Cow"], "Banana")'
python -c 'import script; script.sparse_search(["Alex", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth", "", "", "", "Zachary"], "Parth")'

Code Editor
15161314101112978563412


Terminal


Searchcademy
17/17 Complete
"""

def sparse_search(data, search_val):
  print("Data: " + str(data))
  print("Search Value: " + str(search_val))
  first = 0
  last = len(data)-1
  while first <= last:
    mid = (first+last)//2
    #print("first = {}\n last = {}\n mid = {}".format(first, last, mid))

    if not data[mid]:
      left=mid-1
      right=mid+1

      while True:
        #print("right = {}".format(right))
        #print("left = {}".format(left))
        #if not data[left] == False:
          #break
        #elif not data[right] == False:
          #break
        if left < first and right > last:
          print("! {} is not in the dataset".format(search_val))
          return
        elif right <= last and data[right]:
          mid = right
          #print("mid = {}".format(mid))
          break
        elif left >= first and data[left]:
          mid = left
          #print("mid = {}".format(mid))
          break
        right += 1
        #print("right + 1 = {}".format(right))
        left -= 1
        #print("left - 1 = {}".format(left))
    
    if data[mid] == search_val:
      print("!! {} found at position {}".format(search_val, mid))
      return
    if data[mid] > search_val:
      last = mid - 1
      #print("last = {} - 1  = {}".format(mid, last))
    if data[mid] < search_val:
      first = mid + 1
      #print("first = {} + 1  = {}".format(mid, first))
  
  print("!!! {} is not in the dataset".format(search_val))

sparse_search([""], "Hello")
# nil
sparse_search(["A", "", "", "", "B", "", "", "", "C"], "B")
# 4
sparse_search(["A", "", "", "", ""], "A")
# 0
sparse_search(["", "", "", "", "Z"], "Z")
# 4
sparse_search(["A", "", "", "", "B", "", "", "", "C", "", "", "D"], "C")
# 8
sparse_search(["A", "B", "", "", "E"], "A")
# 0
sparse_search(["", "X", "", "Y", "Z"], "Z")
# 4
sparse_search(["A", "", "", "", "B", "", "", "", "C"], "D")
# nil
sparse_search(["Apple", "", "Banana", "", "", "", "", "Cow"], "Banana")
# 2
sparse_search(["Alex", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth", "", "", "", "Zachary"], "Parth")
# 18
