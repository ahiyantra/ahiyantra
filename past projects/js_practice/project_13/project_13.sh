#!/bin/bash

<< 'MULTILINE-COMMENT'

Skip to Content
My Home
Path Menu
Get Unstuck
Tools



Avatar
Practice JavaScript Syntax: Arrays, Loops, Objects, Iterators: LodashBrief
Objective
JAVASCRIPT SYNTAX, PART II
Lodash
In this project, you will be implementing some of the most exciting functionality from the widely-popular lodash.js library which provides many methods that add new functionality for numbers, strings, objects, and arrays.

If you wanted to use this library in your own projects right now, you could load it, using a Content Delivery Network (CDN) link, in the <head> of your project’s index.html file , like so:

<head>
  <script src='https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js'></script>
  <!-- Make sure that you load lodash before the file that uses it. -->
  <script src='file-that-uses-lodash.js'></script>
</head>
However, implementing the methods from lodash on your own is an invaluable exercise in problem-solving and a great way to understand how the methods work! We’ve selected ten methods for you to implement and, in implementing each method, you will follow these four steps:

Specify the functionality of the method we are implementing
Ideate a game plan for how to implement this functionality in code
Implement our game plan
Test our code to ensure it works as expected
We encourage you to try to complete the “Ideate” and “Implement” steps on your own before consulting our suggestions for each. It may be difficult at points, but working through difficult problems on your own will be incredibly helpful in your journey to become a stronger developer. Once you’ve come up with a solution on your own, or if you have become so stuck you are no longer being productive, check out our steps to see our suggestions for how to solve the problem.

There is no right or wrong answer when it comes to programming. As a result, don’t be frustrated if the solution we present is different than the solution you came up with. We are merely trying to challenge you to consider many different solutions. Your solution is equally as valid as ours. Consider the one you were going to write and then consider ours. Whichever you pick in the end is completely your decision, and we support it completely.

You have the choice of writing this project within the Codecademy environment to the right or locally on your own computer by downloading the starting code here. Feel free to proceed in whichever environment you are most comfortable with.

With all of that said, let’s get started implementing some awesome new functionality!

If you get stuck during this project, check out the project walkthrough video which can be found at the bottom of the page after the final step of the project.

Tasks
43/43 Complete
Mark the tasks as complete by checking them off
Create Lodash Object
1.
Before we get started implementing our new methods, we need to create an object to contain them. This object will represent our library containing all the functionality we add to it.

Create a new variable called _ that is initialized to an empty object.


Stuck? Get a hint
2.
We’ve written test files for each task in this project. Let’s run the first test suite to ensure your lodash object was initialized correctly.

To run a file using node, we type the node command in a command line followed by the name of the file. For example, to run the main file we are working on, we would run node _.js.

Our test files are all located in the test/ directory. To run the test suite for this task, type node test/lodash.js in your terminal and then press enter. The test will either throw errors if something is not currently working properly in your code or will print a success message to the console if your code is good to go.

Implement _.clamp()
3.
Specify: The first method we will implement is .clamp(). Read the explanation and examples of the method in the linked documentation to get a sense of how the method should work.

Here is a summary of the method:

.clamp() takes three arguments: a number, a lower bound, and an upper bound
.clamp() modifies the provided number to be within the two provided bounds
If the provided number is smaller than the lower bound, it will return the lower bound as the final number
If the number is larger than the upper bound, it will return the upper bound as the final number
If the number is already within the two bounds, it will return the number as the final number
You can see a diagram demonstrating this functionality here.

When you’ve ideated a game plan for how to implement this functionality, move on to the next step to see how we plan to do it.

4.
Ideate: There are a number of different ways to implement this method. One that might have come to your mind would be to use control flow to compare the current value and to the bounds and return the proper result. We are going to present a different solution in these steps so that you can keep considering unexpected ways to solve problems.

Add the .clamp() method to the lodash object.

Use Math.max() to clamp the number by the lower bound. The return value of Math.max() called with the number and the lower bound will be the larger of the two values, meaning it will be clamped by the lower bound.

Use Math.min() to clamp the number by the upper bound. The return value of Math.min() called with the number and the upper bound will be the smaller of the two.

Return the final value of these two operations, which will be the clamped number.

Once you have tried implementing this game plan in code, move on to the next step to see how we do it.

5.
Implement: Let’s implement our game plan in code.

Add a method to our _ object called clamp.
Add three parameters to this method: number, lower, and upper.
Within the method, create a variable called lowerClampedValue that is set equal to the return value of Math.max() called with number and lower.
Create a variable called clampedValue that is set equal to the return value of Math.min() called with lowerClampedValue and upper.
Return clampedValue as our final value from the method.
Once you’ve finished implementing this method, move on to the next step to test it.

6.
Test: To test that our .clamp() method works as expected, run node test/clamp.js in your terminal. Don’t worry if any errors appear, work through them one by one until your code runs as expected.

Once all of the tests are passing, congratulate yourself! You’ve implemented the first method of this project! This is very exciting. Hopefully, you’re beginning to feel like a developer.

When you’re ready, move on to the next method.

Implement .inRange()
7.
Specify: The next number method we will implement is .inRange(). Read the explanation and examples of the method in the linked documentation to get a sense of how the method should work.

Here is a summary of the method:

.inRange() takes three arguments: a number, a start value, and an end value
.inRange() checks to see if the provided number falls within the range specified by the start and end values
If the provided number is smaller than the start value, .inRange() will return false
If the provided number is larger than or equal to the end value, .inRange() will return false
If the provided number is within the start and end values, .inRange() will return true
If no end value is provided to the method, the start value will be 0 and the end value will be the provided start value
If the provided start value is larger than the provided end value, the two values should be swapped
When you’ve ideated a game plan for how to implement this functionality, move on to the next step to see how we plan to do it.

8.
Ideate: As always, there are a number of different solutions that could work to solve this problem. This is just one solution.

Add the .inRange() method to the lodash object.
Check to see if the end value is undefined. If so, set the end value equal to the start value and then set the start value equal to 0.
Check to see if the start value is larger than the end value. If so, swap the two values. Note: We will need to use a temporary variable to do this. To understand why, imagine if we tried to swap values without one. We might start by setting the end value equal to the start value. When we then go to set the start value equal to the end value, the end value will have already been overwritten and the swap can’t be completed. To solve this, we create a variable that will temporarily store the end value to access when we need to set the new start value and complete the swap.
Using boolean operators, find out if the number is in the specified range.
Return the value of the previous operation from the method.
Once you have tried implementing this game plan in code, move on to the next step to see how we do it.

9.
Implement: Let’s implement our game plan in code.

Add a method to our _ object called inRange.
Add three parameters to this method: number, start, and end.
Within the method, create an if statement that checks to see if end is undefined.
Within the if statement block, set end equal to start. Then set start equal to 0.
After the previous if statement, add another if statement. This if statement should check whether start is bigger than end.
Within the if statement block, swap the two start and end values. Create a variable called temp that is set to the current end value. Then set end equal to start. Finally, set start equal to temp.
After our second if statement, create a variable called isInRange and set it equal to a boolean expression that checks if start is smaller than or equal to number and if number is smaller than end.
Finally, return the value of isInRange from the method.
Once you’ve finished implementing this method, move on to the next step to test it.

10.
Test: To test that our .inRange() method works as expected, run node test/in-range.js in your terminal. Don’t worry if any errors appear, work through them one by one until your code runs as expected.

Congratulations, you’ve finished implementing all of the number methods!

When you’re ready, move on to the next method.

Implement .words()
11.
Specify: Let’s start implementing some string methods! The first string method we will implement is .words(). We will be writing a slightly modified version of this method to save you some time. Read the explanation and examples of the method in the linked documentation to get a sense of how the method should work. Then read below to see which pieces of functionality you will implement.

Here is a summary of what your method should do:

.words() takes one argument: a string
.words() splits the string into an array of words
A word is defined by a space-separated string of characters, so each space character, ' ', indicates the end of one word and the start of the next
Note: You may have noticed in the documentation that this function has a pattern parameter. Your method does not need to accept the additional pattern parameter, we will only split our string into words based on spaces
When you’ve ideated a game plan for how to implement this functionality, move on to the next step to see how we plan to do it.

12.
Ideate: This solution probably has the most potential solutions of the methods we have implemented thus far. We’ve opted to use a built-in JavaScript method to make this method as short and readable as possible.

Add the .words() method to the lodash object.

Use the string .split() method to split the provided string on space characters into an array of words.

Return the array of words generated in the previous step.

Once you have tried implementing this game plan in code, move on to the next step to see how we do it.

13.
Implement: Let’s implement our game plan in code.

Add a method to our _ object called words.
Add one parameter to this method: string.
Within the method, create a variable called words and set its value equal to string split on space characters ' ' using the .split() method.
Return the value of words from the method.
Once you’ve finished implementing this method, move on to the next step to test it.

14.
Test: To test that our .words() method works as expected, run node test/words.js in your terminal. Don’t worry if any errors appear, work through them one by one until your code runs as expected.

Congratulations! You’ve finished implementing your first string method.

When you’re ready, move on to the next method.

Implement .pad()
15.
Specify: The next string method we will implement is .pad(). We will be writing a slightly modified version of this method to save you some time. Read the explanation and examples of the method in the linked documentation to get a sense of how the method should work. Then read below to see which pieces of functionality you will implement.

Here is a summary of what your method should do:

.pad() takes two arguments: a string and a length
.pad() adds spaces evenly to both sides of the string to make it reach the desired length
Extra padding is added to the end of the string if an odd amount of padding is required to reach the specified length
Your method does not need to accept the additional chars parameter; we will only add space characters to pad our string
You can see a diagram demonstrating this functionality here.

When you’ve ideated a game plan for how to implement this functionality, move on to the next step to see how we plan to do it.

16.
Ideate: Again, as noted with previous game plans, there are many solutions to this problem. We chose this one for readability.

Add the .pad() method to the lodash object.

Check to make sure the target length is longer than the current string length. If not, return the unpadded version of the string.

Find the amount of padding to add to the start of the string by finding the difference between the target length and the string length, dividing by two, and rounding down the resulting number. We round down so that any uneven padding gets added to the end of the string, not the beginning, as specified in the instructions.

Find the amount of padding to add to the end of the string by subtracting the string length and the starting padding length (calculated above) from the target length.

Generate the padded string by adding the amount of starting padding and ending padding calculated above to each side of the current string.

Return the padded version of the string.

Once you have tried implementing this game plan in code, move on to the next step to see how we do it.

17.
Implement: Let’s implement our game plan in code.

Add a method to our _ object called pad.
Add two parameters to this method: string and length.
Within the method, add an if statement that checks if length is shorter than or equal to string‘s length. If so, return string.
Create a variable called startPaddingLength and set its value equal to the difference of length and string‘s length, divided by 2, and rounded down by using Math.floor().
Create a variable called endPaddingLength and set its value equal to length minus string‘s length minus startPaddingLength.
Create a new variable called paddedString and set its value equal to the space character, ' ', repeated startPaddingLength number of times (using the string .repeat() method), concatenated with string, concatenated with the space character repeated endPaddingLength number of times.
Return the value of paddedString from the method.
Once you’ve finished implementing this method, move on to the next step to test it.

18.
Test: To test that our .pad() method works as expected, run node test/pad.js in your terminal. Don’t worry if any errors appear, work through them one by one until your code runs as expected.

Congratulations, you’ve finished implementing all of the new string methods!

When you’re ready, move on to the next method.

Implement _.has()
19.
Specify: Let’s begin implementing some new object methods! The first object method we will implement is .has(). We will be writing a slightly modified version of this method to save you some time. Read the explanation and examples of the method in the linked documentation to get a sense of how the method should work. Then read below to see which pieces of functionality you will implement.

Here is a summary of what your method should do:

.has() takes two arguments: an object and a key
.has() checks to see if the provided object contains a value at the specified key
.has() will return true if the object contains a value at the key and will return false if not
Your method does not need to accept the additional path parameter; we will only check for unnested values
When you’ve ideated a game plan for how to implement this functionality, move on to the next step to see how we plan to do it.

20.
Ideate: Let’s come up with a game plan for implementing this method.

Add the .has() method to the lodash object.

Access the current value at the specified key in the object.

Check to see if the value at that key is undefined.

Return false if the value is undefined and true if not.

Once you have tried implementing this game plan in code, move on to the next step to see how we do it.

21.
Implement: Let’s implement our game plan in code.

Add a method to our _ object called has
Add two parameters to this method: object and key
Within the method, create a variable called hasValue and set its value equal to the result of checking to see if the current value of object at key does not equal undefined.
Return the value of hasValue from the method.
Once you’ve finished implementing this method, move on to the next step to test it.

22.
Test: To test that our .has() method works as expected, run node test/has.js in your terminal. Don’t worry if any errors appear, work through them one by one until your code runs as expected.

Congratulations! You’ve finished implementing the first new object method.

When you’re ready, move on to the next method.

Implement _.invert()
23.
Specify: The next object method we will implement is .invert(). Read the explanation and examples of the method in the linked documentation to get a sense of how the method should work.

Here is a summary of what your method should do:

.invert() takes one argument: an object
.invert() iterates through each key / value pair in the provided object and swaps the key and value
When you’ve ideated a game plan for how to implement this functionality, move on to the next step to see how we plan to do it.

24.
Ideate: Let’s come up with a game plan for implementing this method.

Add the .invert() method to the lodash object.

Create a new object to represent our inverted object.

Iterate through each key in the provided object.

Set the original object’s value at that key to be a key on our inverted object and set the value of that key to be the original object’s key.

Return the inverted object.

Once you have tried implementing this game plan in code, move on to the next step to see how we do it.

25.
Implement: Let’s implement our game plan in code.

Add a method to our _ object called invert.
Add one parameter to this method: object.
Within the method, create a variable called invertedObject and set its value equal to an empty object.
Using a for ... in loop, iterate through each key in object.
Within the loop, create a variable called originalValue and set it equal to the value at the current key in object.
Still within the loop, set the value at originalValue on invertedObject to be the current key.
Finally, outside of the loop, return the value of invertedObject from the method.
Once you’ve finished implementing this method, move on to the next step to test it.


Stuck? Get a hint
26.
Test: To test that our .invert() method works as expected, run node test/invert.js in your terminal. Don’t worry if any errors appear, work through them one by one until your code runs as expected.

Congratulations! When you’re ready, move on to the next method.


Stuck? Get a hint
Implement _.findKey()
27.
Specify: The final object method we will implement is .findKey(). Read the explanation and examples of the method in the linked documentation to get a sense of how the method should work.

Here is a summary of what your method should do:

.findKey() takes two arguments: an object and a predicate function — a function that returns a boolean value
.findKey() iterates through each key / value pair in the provided object and calls the predicate function with the value
.findKey() returns the first key that has a value that returns a truthy value from the predicate function
.findKey() returns undefined if no values return truthy values from the predicate function
When you’ve ideated a game plan for how to implement this functionality, move on to the next step to see how we plan to do it.

28.
Ideate: Let’s come up with a game plan for implementing this method.

Add the .findKey() method to the lodash object.

Iterate through each key in the provided object.

Call the provided predicate function with the value at that key.

If the predicate function returns a truthy value, return the current key from the method.

After the loop, return undefined, since no values returned a truthy value from the predicate function.

Once you have tried implementing this game plan in code, move on to the next step to see how we do it.

29.
Implement: Let’s implement our game plan in code.

Add a method to our _ object called findKey.
Add two parameters to this method: object and predicate. We will name our predicate function parameter predicate since this is the name used in the Lodash documentation.
Within the method, use a for ... in loop to iterate through each key in object.
Within the loop, create a variable called value and set it equal to the value at the current key in object.
Still within the loop, create another variable called predicateReturnValue and set it equal to the result of calling predicate with value.
Finally, still within the loop, use an if statement to check to see if predicateReturnValue is truthy. If it is, return the current key from the method.
Outside of the loop, return undefined to address all cases where no truthy values were returned from predicate.
Once you’ve finished implementing this method, move on to the next step to test it.

30.
Test: To test that our .findKey() method works as expected, run node test/find-key.js in your terminal. Don’t worry if any errors appear, work through them one by one until your code runs as expected.

Congratulations, you’ve implemented all of the object methods! These are starting to get a little tricky. If you’re feeling overwhelmed at all, that’s normal. Just keep tackling these problems one at a time, and you’ll soon find that you’ll be able to tackle problems like these faster and faster.

When you’re ready, move on to the next method.

Implement _.drop()
31.
Specify: It’s time to start implementing methods for our final data type: arrays! The first array method we will implement is .drop(). Read the explanation and examples of the method in the linked documentation to get a sense of how the method should work.

Here is a summary of what your method should do:

.drop() takes two arguments: an array and a number representing the number of items to drop from the beginning of the array
.drop() returns a new array which contains the elements from the original array, excluding the specified number of elements from the beginning of the array
If the number of elements to drop is unspecified, your method should drop one element
When you’ve ideated a game plan for how to implement this functionality, move on to the next step to see how we plan to do it.

32.
Ideate: Let’s come up with a game plan for implementing this method.

Add the .drop() method to the lodash object.

Check to see if the number of items to drop was set. If not, set the number equal to 1.

Create a new copy of the original array with the specified number of elements dropped from the beginning of the array. We will use the array .slice() method to accomplish this.

Return the modified copy of the array from the method.

Once you have tried implementing this game plan in code, move on to the next step to see how we do it.

33.
Implement: Let’s implement our game plan in code.

Add a method to our _ object called drop.
Add two parameters to this method: array and n.
Within the method, use an if statement to check if n has been set.
Within the if statement block, set n equal to 1.
Outside of the if statment, create a new variable called droppedArray and set its value to be a copy of the array missing the first n elements by using .slice().
Return droppedArray from the method.
Once you’ve finished implementing this method, move on to the next step to test it.

34.
Test: To test that our .drop() method works as expected, run node test/drop.js in your terminal. Don’t worry if any errors appear, work through them one by one until your code runs as expected.

Congratulations, you’ve implemented the first array method!

When you’re ready, move on to the next method.

Implement _.dropWhile()
35.
Specify: The next array method we will implement is .dropWhile(). Read the explanation and examples of the method in the linked documentation to get a sense of how the method should work.

Here is a summary of what your method should do:

.dropWhile() takes two arguments: an array and a predicate function
The supplied predicate function takes three arguments: the current element, the current element index, and the whole array
.dropWhile() creates a new copy of the supplied array, dropping elements from the beginning of the array until an element causes the predicate function to return a falsy value
When you’ve ideated a game plan for how to implement this functionality, move on to the next step to see how we plan to do it.

36.
Ideate: Let’s come up with a game plan for implementing this method.

Add the .dropWhile() method to the lodash object.

Iterate through the array until you find an element that causes the predicate to return a falsy value. We will use .findIndex() to iterate through the array since it is built to iterate through an array until it finds an element that returns a specific value.

Use our previous .drop() method to drop the elements prior to the one that returned a falsy value.

Return the modified copy of the array from the method.

Once you have tried implementing this game plan in code, move on to the next step to see how we do it.

37.
Implement: Let’s implement our game plan in code.

Add a method to our _ object called dropWhile.
Add two parameters to this method: array and predicate.
Within the method, create a new variable called dropNumber and set its value equal to the return value of a call to findIndex on array.
Pass an anonymous callback function to findIndex that takes two arguments: element and index.
Within the callback function, return the negated return value of predicate called with element, index, and array. We negate the value (use !) since we are looking to drop elements until the predicate returns a falsy value. However, .findIndex() is looking for the first truthy value. So, we make every truthy value falsy and vice versa to get the value we are looking for.
After the entire dropNumber declaration, create a new variable called droppedArray and set its value to the return value of this.drop() called with dropNumber. We are using this since .drop() is a method on the _ object which is the current object we are working from, and therefore the current value of this. Calling _.drop() would also have worked but is a less common practice.
Return droppedArray from the method.
Once you’ve finished implementing this method, move on to the next step to test it.

38.
Test: To test that our .dropWhile() method works as expected, run node test/drop-while.js in your terminal. Don’t worry if any errors appear, work through them one by one until your code runs as expected.

Congratulations! This method wasn’t especially long, but it used a lot of advanced concepts. Great job working through it!

When you’re ready, move on to the next method.

Implement _.chunk()
39.
Specify: The last array method we will implement is .chunk(). Read the explanation and examples of the method in the linked documentation to get a sense of how the method should work.

Here is a summary of what your method should do:

.chunk() takes two arguments: an array and a size
.chunk() breaks up the supplied array into arrays of the specified size
.chunk() returns an array containing all of the previously-created array chunks in the order of the original array
If the array can’t be broken up evenly, the last chunk will be smaller than the specified size
If no size is supplied to the method, the size is set to 1
You can see a diagram demonstrating this functionality here.

When you’ve ideated a game plan for how to implement this functionality, move on to the next step to see how we plan to do it.

40.
Ideate: Let’s come up with a game plan for implementing this method.

Add the .chunk() method to the lodash object.

Check to see if a size has been supplied. If not, set the size equal to 1.

Create an empty array that will contain all of the generated array chunks.

Loop through the array. In each turn of the loop, create an array chunk of the specified size, add it to the final array, and increase the loop counter by the chunk size to go to the next chunk. We will use a for loop to do this, since no iterator method does exactly what we want and a while loop won’t auto-increment.

Return the array of array chunks from the method.

Once you have tried implementing this game plan in code, move on to the next step to see how we do it.

41.
Implement: Let’s implement our game plan in code.

Add a method to our _ object called chunk.
Add two parameters to this method: array and size.
Within the method, write an if statement that checks to see if size is undefined.
Within the if statement block, set size equal to 1.
After the if statement, create a variable called arrayChunks and initialize it to an empty array.
Write a for loop that loops through array and has a counter that increments by size each turn of the loop.
Within the for loop, create a variable called arrayChunk and set it equal to the chunk of the array going from the current loop index to the current loop index plus size. You an use .slice() to accomplish this.
Still within the for loop, add arrayChunk to the end of arrayChunks. You can use .push() to accomplish this.
Finally, outside of the for loop, return arrayChunks from the method.
Once you’ve finished implementing this method, move on to the next step to test it.

42.
Test: To test that our .chunk() method works as expected, run node test/chunk.js in your terminal. Don’t worry if any errors appear, work through them one by one until your code runs as expected.

Congratulations, you’ve implemented all of the methods of this project! This is a huge accomplishment.

We hope you now have the confidence to go out and build your own multi-million-download open-source library! It may seem like a crazy statement at this stage in your coding journey, but you’ve demonstrated you have the skills to do it.

What’s next for this project? We suggest you try implementing even more methods from the lodash library and address additional edge cases for the methods you wrote. We also encourage you to clean up your code by following the Google JavaScript style guidelines. Making sure your code is easy to read and follows best practices is a great way to set yourself apart as a developer.

Take a moment to congratulate yourself on how far you’ve come. You truly deserve it!

43.
If you are stuck on the project or would like to see an experienced developer work through the project, watch the following project walkthrough video!



Code Editor

files
test
_.js

Code Editor

Terminal

43/43 Complete
Back

MULTILINE-COMMENT

node test/lodash.js
node test/clamp.js
node test/in-range.js
node test/words.js
node test/pad.js
node test/has.js
node test/invert.js
node test/find-key.js
node test/drop.js
node test/drop-while.js
node test/chunk.js

<< 'MULTILINE-COMMENT'

$ node test/lodash.js
Lodash Object Tests:
1 - _ is defined - Passed!
2 - The value of _ is an object - Passed!
$ 
$ node test/clamp.js
_.clamp() Tests:
1 - _.clamp() is defined - Passed!
2 - Returns in-range values unclamped - Passed!
3 - Clamps values by lower bound - Passed!
4 - Clamps values by upper bound - Passed!
$ 
$ node test/in-range.js
_.inRange() Tests:
1 - _.inRange() is defined - Passed!
2 - Returns true if an in-range value is in range - Passed!
3 - Returns false if a too small value is out of range - Passed!
4 - Returns false if a too large value is out of range - Passed!
5 - Uses end value as start value and start value as 0 if end value is not defined - Passed!
6 - Reverses start and end values if start is bigger than end - Passed!
7 - Returns true if provided value is same as start value - Passed!
8 - Returns false if provided value is same as end value - Passed!
$ 
$ node test/words.js
_.words() Tests:
1 - _.words() is defined - Passed!
2 - Returns an array - Passed!
3 - Returns an array of words from a string with one word - Passed!
4 - Returns an array of words from a string with two words - Passed!
5 - Returns an array of words from a string with three words - Passed!
$ 
$ node test/pad.js
_.pad() Tests:
1 - _.pad() is defined - Passed!
2 - Returns evenly-padded strings - Passed!
3 - Returns oddly-padded strings with extra padding on right side - Passed!
4 - Returns strings longer than provided length un-padded - Passed!
$ 
$ node test/has.js
_.has() Tests:
1 - _.has() is defined - Passed!
2 - Returns true if an object has a value at a specified key - Passed!
3 - Returns false if an object does not have a value at a specified key - Passed!
$ 
$ node test/invert.js
_.invert() Tests:
1 - _.invert() is defined - Passed!
2 - Returns an object with key and value inverted for a single key-value pair - Passed!
3 - Original key is not present after the key-value pairs have been inverted - Passed!
4 - Returns an object with all keys and values inverted - Passed!
$ 
$ node test/find-key.js
_.findKey() Tests:
1 - _.findKey() is defined - Passed!
2 - Returns the corresponding key of a value that returns truthy from the predicate function - Passed!
3 - Returns undefined if an object has no values that return truthy from the predicate function - Passed!
$ 
$ node test/drop.js
_.drop() Tests:
1 - _.drop() is defined - Passed!
2 - Returns an array - Passed!
3 - Drops the specified number of elements from the beginning of an array - Passed!
4 - Drops one element if no number is specified - Passed!
$ 
$ node test/drop-while.js
_.dropWhile() Tests:
1 - _.dropWhile() is defined - Passed!
2 - Returns an array - Passed!
3 - Drops elements until predicate function returns falsy - Passed!
$ 
$ node test/chunk.js
_.chunk() Tests:
1 - _.chunk() is defined - Passed!
2 - Returns an array - Passed!
3 - Chunks evenly-divided arrays - Passed!
4 - Chunks unevenly-divided arrays - Passed!
$ 

MULTILINE-COMMENT
