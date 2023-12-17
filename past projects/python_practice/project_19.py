"""

Learn Complex Data Structures

Avatar
Learn Complex Data Structures: BlossomBrief
Objective
LEARN COMPLEX DATA STRUCTURES
Blossom
The language of the flowers has a long history and has often been a topic resigned to the domain of dusty books in a thrift bookseller or a library. With Blossom, we want to give people lightning fast access to all of the possible meanings of their favorite flowers.

In this project, we are going to implement a hash map to relate the names of flowers to their meanings. In order to avoid collisions when our hashing function collides the names of two flowers, we are going to use separate chaining. We will implement the Linked List data structure for each of these separate chains.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
26/26 Complete
Mark the tasks as complete by checking them off
Building Out The Hash Map
1.
The underlying data structure for Blossom is going to be a key-value store that uses the common names for flowers as the key and saves the floral meaning of the flower as the value.

In order to implement this functionality, we’re going to build out a hash map with separate chains of linked lists at every index.

First, let’s define our HashMap class.


Stuck? Get a hint
2.
The first thing that we’ll need for our hash map is an array. Python’s lists behave similar to an array, but we’ll need to keep track and enforce the list’s size to make the resemblance stronger.

Give HashMap a constructor that takes a size parameter. Save size into self.array_size.

After that, create a list of None objects of length size and save it into self.array.


Stuck? Get a hint
3.
In order to implement a hash map, we need to implement four different methods.

The first two are the internal methods needed to perform the basic responsibilities of a hash map: .hash() and .compress().

The next two are the external methods someone interacting with the hash map will use: .assign() and .retrieve().

Let’s start by implementing a basic hash function. When the key is a string (which is true for all of Blossom’s keys) we’ll need to calculate a number for that string. Let’s sum up the character encodings of each character in the string and use that.

Define a method called .hash() that takes both self and key as parameters.

4.
Calculate the hash code for the key by calling key.encode() and performing the sum on the resulting list-like object.


Stuck? Get a hint
5.
Now that we have a hash function, that returns a number, we’ll also need a compression function that reduces this number into an array index.

Define a .compress() method that takes a hash_code parameter. Return the result of calculating the remainder of dividing hash_code by self.array_size.


Stuck? Get a hint
6.
With our hash and compression functions written, all we need to create a basic hash map are our .assign() and .retrieve() methods. Let’s start with .assign().

Define a .assign() method that takes three parameters: self, key, and value. Get the hash code by plugging key into .hash() and then get the array index by plugging the resulting hash code into .compress(). Save the result into the variable array_index.

7.
In the array, at the address array_index, save both the key and the value as a list: [key, value].

8.
Now that we have an assignment function, let’s also build out our retrieval function.

Define a .retrieve() method that takes two parameters: self and key.

9.
.retrieve() should find the hash code for key by plugging it into .hash() and then find the array index by plugging that hash code into .compress().

Save that index into a variable called array_index

10.
Save the value of self.array at array_index into a variable called payload.

11.
If payload is not None, then we know it’s a list that looks like [key, value].

Check the first item (payload[0]) and compare it with key. If they are the same, return the second item in payload (the value!).

If payload is None or the first item is not the same as key, return None.

Adding in the Linked List
12.
Let’s add in the separate chaining aspect of our algorithm. Import the linked list and node library by calling

from linked_list import Node, LinkedList
At the top of script.py

13.
In HashMap.__init__, find the line where we created a list of None objects.

Change this so that self.array instead is a list of LinkedLists.

The resulting self.array should be a Python list of LinkedList objects, make sure to instantiate them.


Stuck? Get a hint
Adding in Separate Chaining: Assignment
14.
In .assign(), we’re going to be replacing the assign logic after getting the array_index from the .hash() and .compressor() methods.

Create a new Node object with value [key, value]. Assign that Node object to a variable called payload.


Stuck? Get a hint
15.
We’ll need to check if the key exists in the LinkedList before we add our new payload to it. Save self.array[array_index] into the variable list_at_array.


Stuck? Get a hint
16.
Iterate through list_at_array using a for loop. For every item in list_at_array, check if the key (the element at index 0) is the same as the key we’re trying to assign.


Stuck? Get a hint
17.
If we do find a key at one of the items in the linked list, overwrite its value with value.


Stuck? Get a hint
18.
If we’ve iterated through the list and not found our key, we need to add it.

Remove the line where we assign

self.array[array_index] = [key, value]
And change it so that we use list_at_array.insert() to insert the payload to our chained list.


Stuck? Get a hint
Adding in Separate Chaining: Retrieval
19.
Now we’re going to update .retrieve() to use separate chaining. We’re going to rewrite the code after we get our array_index.

Using the array_index variable, get the LinkedList object at that index in self.array. Before we called this payload but since it represents a different type of object, let’s name it something different.

Save the result into a variable called list_at_index.

20.
Iterate through the linked list similarly to how .assign() did, checking the key in each part of the list to see if it’s the same as our key.


Stuck? Get a hint
21.
If you do find the key, return the value (at index 1 in the node’s value), otherwise return None!

Adding the Flower Definitions
22.
Now lets add in some flower definitions! Use

from blossom_lib import flower_definitions 
To import the flower definitions.

23.
Now let’s create a new instance of our HashMap create an instance called blossom. Make the list of our new HashMap the same length as flower_definitions.


Stuck? Get a hint
24.
Now, for every element of flower_definitions, assign the value (index 1) to its key (index 0) using blossom.assign().


Stuck? Get a hint
25.
Now use our app! Look up a flower’s meaning using blossom.retrieve('daisy'). Try printing it out!

Does it work? Next, try looking up another flower. Is the flower you’re looking for missing? How would you add it in?

26.
If you are stuck on the project or would like to see an experienced developer work through the project, watch the following project walkthrough video!


Code Editor
28293031323334353637384042434439414546


Output-only Terminal
Output:
 

Blossom
26/26 Complete

"""

from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for v0 in range(0, self.array_size)]
  def hash(self, key):
    self.hash_code = sum(key.encode())
    return self.hash_code
  def compress(self, hash_code):
    self.index = hash_code % self.array_size
    return self.index
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    #self.array[array_index] = [key, value]
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for v0 in list_at_array:
      if v0[0] == key:
        v0[1] = value
    list_at_array.insert(payload)
  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    #payload = self.array[array_index]
    list_at_index = self.array[array_index]
    for v0 in list_at_index:
      if v0[0] == key:
        return v0[1]
      else:
        return None
    if payload == None:
      return None
    else:
      if payload[0] == key:
        return payload[1]

blossom = HashMap(len(flower_definitions))

print(flower_definitions)

for v0 in flower_definitions:
  blossom.assign(v0[0], v0[1])

print(blossom.retrieve('daisy'))
