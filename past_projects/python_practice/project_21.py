"""

Learn Complex Data Structures

Avatar
Learn Complex Data Structures: Maze ExplorerBrief
Objective
LEARN COMPLEX DATA STRUCTURES
Maze Explorer
Welcome Ancient Ruins Explorer!

We’ve identified a mysterious chamber deep underground our excavation site. The artifacts held within this chamber would be a considerable addition to the local museum…

Unfortunately, the chamber lies at the heart of a twisted maze. We’re using a graph data structure to model the ruins. We’ll need your expertise to map out the chambers as we move through them.

With your help, we’ll find the optimal path to the chamber before our torch burns out.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
37/37 Complete
Mark the tasks as complete by checking them off
Gearing up!
1.
Our team has supplied you with Graph and Vertex classes, and you’ll be working from script.py.

Tab around to get oriented, then make an excavation_site variable inside script.py and assign it to the build_graph() function we’ve supplied.

2.
Save your work, then type python3 script.py in the terminal to run your code.

MAZE LAYOUT should print in the terminal.

If your terminal ever gets too mucked up, click into the terminal and type control + l to clean it up.

3.
Let’s take our first steps into the maze. Tab over to graph.py.

Inside the build_graph() function, we’ll make vertices for each room in the maze. We know there’s an entrance, so let’s start there.

Below the line # MAKE ROOMS INTO VERTICES BELOW..., make a variable entrance and set it to an instance of Vertex with "entrance" as an argument.


Stuck? Get a hint
4.
Now that we have an instance of Vertex, we need to add it to our graph.

Below the line, # ADD ROOMS TO GRAPH BELOW..., use .add_vertex() to add entrance to graph.


Stuck? Get a hint
5.
Let’s test it out.

Save your work and run python3 script.py.

If everything goes according to plan you should see entrance connected to... printed to the terminal.

Congratulations, explorer. We’re ready to enter the maze…

Entering the maze.
6.
You bravely set foot inside the entrance and see two paths.

After a little scouting, you identify these new rooms as an "ante-chamber" and the "king's room".

We need to add your discoveries to build_graph().

Make a variable ante_chamber and set it to an instance of Vertex with "ante-chamber" as the argument.

Add the vertex, ante_chamber, to the graph.

7.
Make a variable kings_room and set it to an instance of Vertex with "king's room" as the argument.

Add the vertex, kings_room, to the graph.

8.
Save your work and run python3 script.py.

You should see each of the rooms listed, but they’re not connected!

9.
We’re using a Graph instance to track our rooms.

Each room is a vertex. If we can travel from one room to another, that means an edge exists!

Use the .add_edge() method within Graph to set up these connections:

entrance is connected to ante_chamber with a weight of 7.
entrance is connected to kings_room with a weight of 3.

Stuck? Get a hint
10.
Save your work and run python3 script.py in the terminal. You should see the connections listed now.

11.
While reviewing the chambers, you discover a passage between kings_room and ante_chamber. Update the build_graph() function with this new edge.

kings_room is connected to ante_chamber with a weight of 1.
Mapping the maze
12.
Emboldened by your recent discoveries, you explore deeper into the chambers.

You unearth a grand_gallery.

Expand our build_graph() function so it includes the variable grand_gallery set to an instance of Vertex with"grand gallery" as an argument.

13.
Add grand_gallery as a vertex to graph.

Then set the edges:

grand_gallery is connected to ante_chamber with a weight of 2.
grand_gallery is connected to kings_room with a weight of 2.
14.
Weary but exhilarated, you come across the treasure room!

Update build_graph() with the last chamber, make an instance of Vertex with the argument "treasure room" and assign it to the variable treasure_room.

Add the vertex, treasure_room to the graph.

15.
Inside build_graph(), set the edges for the newly discovered treasure_room.

treasure_room is connected to ante_chamber with a weight of 6.
treasure_room is connected to grand_gallery with a weight of 4.
16.
Save your work and see the fully mapped out maze by running python3 script.py in the terminal.

Exploring the Maze
17.
You’ve mapped out all the chambers in the maze, but in all the excitement you forgot exactly how to get to treasure_room from entrance.

Let’s fill in the .explore() method in Graph to help you out.

18.
In this method, create a variable called current_room and set it equal to 'entrance'.

Next, create a variable called path_total and set it equal to 0.

19.
Now create a print statement with the following text:

"\nStarting off at the {0}\n". such that the {0} should hold the value of current_room.

Stuck? Get a hint
20.
Tab back to script.py and call the .explore() method on excavation_site.

Save your work and run python3 script.py in the terminal. The output should first map out the maze and then print "Starting off at the entrance".

21.
Now, we want to keep navigating the maze until we find the 'treasure room'. Make a while loop that checks if the current_room is NOT equal to 'treasure room'.

22.
In the while loop, we first want to retrieve all the data of the current_room.

Create a variable called node and set it equal to the values corresponding to the current_room in the graph dictionary.


Stuck? Get a hint
23.
After entering a room, we want to check the adjacent rooms.

Create a for loop that iterates through the items of the node’s edges and retrieves each connected_room and weight.

Check the hint for a solution.


Stuck? Get a hint
24.
In this for loop, we will show the user all the choices of rooms they can move to and their respective costs.

Let’s make it easy for the user and have the first letter of each room correspond to the room itself.

In the for loop, create a variable key and set it equal to the first letter of the connected_room.


Stuck? Get a hint
25.
In the for loop, print the following statement:

"enter {0} for {1}: {2} cost"
{0} corresponds to key. {1} corresponds to connected_room. {2} corresponds to weight.


Stuck? Get a hint
26.
Outside the for loop, but still in the while loop, we want to now gather the user’s input.

Create a variable called valid_choices and set it equal to a list of all the first letters of the keys of the node’s edges. Try using a list comprehension.

Check the hint for a solution.


Stuck? Get a hint
27.
Now, print the following:

"\nYou have accumulated: {0} cost"
{0} corresponds to path_total.

28.
Now, we want to see what room the user wants to move to.

Create a variable choice and set it equal to the input of the following string:

"\nWhich room do you move to? "

Stuck? Get a hint
29.
Save your work and run python3 script.py in the terminal. The output should have the previous outputs and also prompt you to enter a choice.

30.
Now, we will check to see if the user did NOT enter valid choice.

Back in graph.py, still within the while loop, create an if statement that checks if choice is NOT in valid_choices.

If so, print the following:

"please select from these letters: {0}"
{0} corresponds to valid_choices.

31.
Now, create an else clause. This means the user selected a valid choice.

In the else clause, create a for loop that iterates through the keys of the node’s edges and retrieves each room.

Check the hint for the solution.


Stuck? Get a hint
32.
In the for loop, create an if statement that checks if the first letter of the room is the user’s choice.

You can use the .startswith() method.


Stuck? Get a hint
33.
In the if statement, set current_room equal to the room.

34.
Also within the if statement, update path_total to itself plus the edge weight between the node and the room. Use the edges dictionary!

Check the hint for a solution.


Stuck? Get a hint
35.
Outside the for loop, but still within the else clause, print the following:

"\n*** You have chosen: {0} ***\n"
{0} corresponds to the current_room.

36.
Finally, outside the while loop, print the following:

"Made it to the treasure room with {0} cost"
{0} corresponds to the path_total.

37.
Congratulations! You have finished the project!

Save your work and run python3 script.py in the terminal. Explore the maze to try and find the shortest path to the treasure!

Code Editor
123456789


Terminal


Maze Explorer
37/37 Complete

"""

--------------------------------------------------
# "script.py"
--------------------------------------------------

# import classes
from graph import Graph, build_graph
from vertex import Vertex

excavation_site = build_graph()

excavation_site.explore()

--------------------------------------------------
# "graph.py"
--------------------------------------------------

from vertex import Vertex

class Graph:
  def __init__(self):
    self.graph_dict = {}

  def add_vertex(self, node):
    self.graph_dict[node.value] = node

  def add_edge(self, from_node, to_node, weight = 0):
    self.graph_dict[from_node.value].add_edge(to_node.value, weight)
    self.graph_dict[to_node.value].add_edge(from_node.value, weight)

  def explore(self):
    print("Exploring the graph....\n")
    #FILL IN EXPLORE METHOD BELOW
    current_room = 'entrance'
    path_total = 0
    print("\nStarting off at the {}\n".format(current_room))
    while current_room != 'treasure room':
      node = self.graph_dict[current_room]
      for connected_room, weight in node.edges.items():
        key = connected_room[0]
        print("enter {} for {}: {} cost".format(key, connected_room, weight))
      valid_choices = [v[0] for v in node.edges.keys()]
      print("\nYou have accumulated: {} cost".format(path_total))
      choice = input("\nWhich room do you move to? ")
      if (choice in valid_choices) == False:
        print("please select from these letters: {}".format(valid_choices))
      else:
        for room in node.edges.keys():
          if room[0] == choice:
            current_room = room
            path_total += node.edges[room]
        print("\n*** You have chosen: {} ***\n".format(current_room))
    print("Made it to the treasure room with {} cost".format(path_total))
  
  def print_map(self):
    print("\nMAZE LAYOUT\n")
    for node_key in self.graph_dict:
      print("{0} connected to...".format(node_key))
      node = self.graph_dict[node_key]
      for adjacent_node, weight in node.edges.items():
        print("=> {0}: cost is {1}".format(adjacent_node, weight))
      print("")
    print("")

def build_graph():
  graph = Graph()
  
  # MAKE ROOMS INTO VERTICES BELOW...
  entrance = Vertex("entrance")
  ante_chamber = Vertex("ante-chamber")
  kings_room = Vertex("king's room")
  grand_gallery = Vertex("grand gallery")
  treasure_room = Vertex("treasure room")

  # ADD ROOMS TO GRAPH BELOW...
  graph.add_vertex(entrance)
  graph.add_vertex(ante_chamber)
  graph.add_vertex(kings_room)
  graph.add_vertex(grand_gallery)
  graph.add_vertex(treasure_room)

  # ADD EDGES BETWEEN ROOMS BELOW...
  graph.add_edge(entrance, ante_chamber, 7)
  graph.add_edge(entrance, kings_room, 3)
  graph.add_edge(kings_room, ante_chamber, 1)
  graph.add_edge(grand_gallery, ante_chamber, 2)
  graph.add_edge(grand_gallery, kings_room, 2)
  graph.add_edge(treasure_room, ante_chamber, 6)
  graph.add_edge(treasure_room, grand_gallery, 4)

  # DON'T CHANGE THIS CODE
  graph.print_map()
  return graph

--------------------------------------------------
# "vertex.py"
--------------------------------------------------

class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, adjacent_value, weight = 0):
    self.edges[adjacent_value] = weight

  def get_edges(self):
    return self.edges.keys()
