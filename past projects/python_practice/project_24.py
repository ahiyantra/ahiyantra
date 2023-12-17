"""
Skip to Content
Basic Graph Search Algorithms


Avatar
Basic Graph Search Algorithms : SkyRoute: A Graph Search ProgramBrief
Objective
GRAPH SEARCH ALGORITHMS
SkyRoute: A Graph Search Program
Vancouver’s public metro system has asked you to help create a program to help commuters get from one landmark to another. You’ll be building out “SkyRoute,” a routing tool that uses breadth-first search, depth-first search, and Python dictionaries to accomplish this feat. For the purposes of this project, you can assume that it takes the same amount of time to get from each station to each of its connected neighboring stations.

First, tab through the files you have at your disposal:

graph_search.py has the bfs() and dfs() functions implemented in Python
vc_metro.py contains a graph of all stations in the Vancouver metro system
vc_landmarks.py contains a dictionary of Vancouver landmarks mapped to their nearest metro station(s)
landmark_choices.py contains a dictionary of letters of the alphabet mapped to landmarks to make it easier for users to make a selection
We’ve imported these for you into skyroute.py, which is where you’ll be building out the SkyRoute tool.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
50/50 Complete
Mark the tasks as complete by checking them off
1.
First, define a variable that we’ll be using throughout our program:

landmark_string should be a string that joins all of the landmarks together, each with its corresponding letter of the alphabet from landmark_choices on a new line.


Stuck? Get a hint
2.
Below landmark_string, define a function greet() with no parameters. In the function body, print out two statements:

"Hi there and welcome to SkyRoute!"
"We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string
See how that landmark_string already came in handy?

3.
Outside of greet(), define a new function skyroute() which will contain our full program. It won’t take any parameters. Inside, call greet().

Great! Now, try calling skyroute() at the bottom of the file, save your code, and enter python3 skyroute.py in your console to see what happens.

4.
Let’s jump out of the skyroute() function body and define a few new functions. Add pass into the function body for each for the moment.

First, set_start_and_end(), which takes two parameters: start_point and end_point. This will handle setting the selected origin and destination points.
Next, get_start(), which takes no parameters. It will be used to request an origin from the user.
Finally, get_end(), which is also void of parameters. Can you guess how it will be used?
5.
In the function body of set_start_and_end(), remove pass and check if start_point has a value other than None. If it does, we already have an origin and destination, but the user wants to make a change. Luckily, we’re prepared for that!

Collect input from the user using the following question and assign the response to a new variable change_point:

"What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': "


Stuck? Get a hint
6.
Before we handle change_point, add an else condition in case no start_point has been set yet. Inside the else condition:

set start_point equal to get_start()
set end_point equal to get_end() Below the else condition (outside of it, but still inside the function), employ multiple return to return both start_point and end_point from the function.

Stuck? Get a hint
7.
Now let’s get back into that if statement and tackle change_point. Below your definition of change_point, we’ll add a little control flow to handle the input:

If change_point is equal to "b", then reset start_point and end_point using get_start() and get_end() respectively.
Use elif to check if change point is "o". If it is, then only reset start_point.
Use another elif statement to check if change point is "d". If it is, then only reset end_point.
Use else to handle cases in which the user typed some other value. Inside the condition, print "Oops, that isn't 'o', 'd', or 'b'..." and recursively call set_start_and_end() on start_point and end_point so that the user has a chance to try again.

Stuck? Get a hint
8.
Try calling set_start_and_end() with None and None as the arguments and printing the result. Save your code and enter python3 skyroute.py in the terminal to see what happens!

After all that work, why are you getting back "None, None"? Oh right, you still need to set up get_start() and get_end()! The good news is that these functions are very similar.

Make sure to remove your call of set_start_and_end().

9.
Let’s begin with get_start(). In the function body, remove pass and set start_point_letter equal to user input from the question "Where are you coming from? Type in the corresponding letter: ".

We need to make sure make sure the user entered a real landmark name! Use a conditional to check if start_point_letter exists as a key in landmark_choices.

If it does, set start_point equal to landmark_choices[start_point_letter] and return start_point from the function.

10.
Add an else condition. In the body of the else condition, print "Sorry, that's not a landmark we have data on. Let's try this again..." and recursively return a call of get_start() so that the user gets a chance to get it right.

11.
Set up get_end() in exactly the same way as you set up get_start() except with:

end_point in lieu of start_point
a recursive call of get_end() in lieu of get_start()
"Ok, where are you headed? Type in the corresponding letter: "
instead of "Where are you coming from? "
12.
Try calling set_start_and_end() with None and None as the arguments and printing the result to the console again. Did you get the right return values?


Stuck? Get a hint
13.
Let’s build a wrapper function for the bulk of the program that we can use to:

get and set the origin and destination
call search to get the recommended route
allow users to search for another route
To accomplish this, define a new function new_route(), which takes two parameters: start_point and end_point. Give both a default value of None.

We do this because start_point and end_point may need to be defined for the first time or redefined upon subsequent new_route() calls.

14.
In the new_route() function, set start_point and end_point equal to the function call of set_start_and_end() with start_point and end_point as arguments.


Stuck? Get a hint
15.
We have the function to set the origin and destination for our route. It’s time for a bit of breadth-first search to spice things up and actually find the best route between those selected points!

Outside new_route(), define a new function get_route() which takes two parameters. Can you guess what they are?


Stuck? Get a hint
16.
You may be itching to run bfs() on your start and end points (with the vc_metro graph). You can even try it out, but if you run that code, you won’t get what you’re looking for. That is, unless what you’re looking for happens to be a pile of errors.

Why all the errors?

Your start_point and end_point are landmarks, not metro stations. And if you take a look at vc_landmarks.py again, you’ll see that some landmarks have more than one metro station. In order to get the metro stations closest to to each landmark, you’ll need to access them through the vc_landmarks dictionary.

Inside the get_route() function, create a variable start_stations and set it equal to vc_landmarks[start_point]. This should grab a set of at least one metro station.

17.
Below start_stations, set another variable end_stations using the same logic.

18.
Because some landmarks have more than one station, there is sometimes more than one route between landmarks. That means it’s our job to collect all of the shortest routes between stations and then compare them based on path length.

For example, you could get from Herald Square in Midtown, NYC to Codecademy in Soho, NYC in a few ways. You can start at 34th Street-Herald Square station and end either at Prince Street station or Broadway-Lafayette station.

The shortest path between 34th Street-Herald Square and Prince Street is five stops. The shortest path between 34th Street-Herald Square and Broadway-Lafayette is two stops. If we compare those two possible shortest routes, we have a clear shortest route.

To collect our shortest routes for comparison, create an empty list called routes under the stations variables you just defined in get_route().

19.
Ready to get your loop on? To get each combination, we can use a Python for loop to loop through each start_station in start_stations and then, inside, loop through each end_station in end_stations.

20.
Inside the inner for loop, create a variable route and set it equal to a call of bfs() on vc_metro as the graph, start_station as the start vertex, and end_station as the end vertex.

21.
Check if route exits. If it does, add this new shortest route to the routes list that you created. If you’ll recall, this route returned from bfs() is a Python list that represents the path.

22.
Outside of both loops but still inside the get_route() function, we can now get our shortest route from our routes list based on list length using a nifty Python trick:

min(list_name, key=len)
Save the final resulting shortest route to a variable shortest_route and then return shortest_route from the function.

23.
Let’s see if the get_route() function does what it’s supposed to! Call get_route() with two landmark names (you can grab these from the vc_landmarks keys) and print the result. Now save your code and in the console enter: python3 skyroute.py.

24.
It’s time to take this awesomeness back to the new_route() function. In your new_route() function body, create a variable shortest_route and set it equal to get_route() called on the start_point and end_point variables you defined above.

25.
As you may have noticed, shortest_route is in a format that isn’t all that user-friendly. Let’s change that! Create a new variable called shortest_route_string set to a string that has each station from shortest_route on a new line. Hint:

some_string = '\n'.join(list_name)
26.
Below this new string variable, print the following to the console:

"The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string)
27.
At this point, we have a pretty solid tool. Call new_route() in the body of skyroute() below greet(). Now try calling skyroute() in your console. Pretty cool, right?

28.
What if someone wants to know about more than one route? Let’s give them a chance to get that info before the program abruptly closes down. Under the final print statement in new_route(), collect user input for the question "Would you like to see another route? Enter y/n: " and save it to the variable again.

29.
Check if again is equal to “y”. If it is, make a recursive call of new_route() with the current values of start_point and end_point passed in.

30.
After a few calls, it might be helpful for the user to see the list of landmarks again. Above the recursive call of new_route(), call a function show_landmarks() without any arguments.

31.
Outside of new_route(), define show_landmarks() without any parameters. In the function body, use a new variable see_landmarks to capture user input for the question "Would you like to see the list of landmarks again? Enter y/n: ".

32.
On the next line (still in the show_landmarks() function), check if see_landmarks is equal to “y”. If it is, print out the landmark_string for the user.

33.
Now our function will loop as long as our user wants to look up new directions! Pretty neat, right? But we still have a bit of an abrupt ending. Let’s fix that. Outside all your functions, create another function goodbye(). In it, print "Thanks for using SkyRoute!", giving our user some pleasant parting words.

34.
Add a call of goodbye() at the end of the skyroute() function body. Test out your function in the console to see how it works!


Stuck? Get a hint
35.
Great news. Vancouver’s public metro system loves the tool you created. However, the system is now about to get slammed with some much-needed repair work. Your metro contact wants to know:

Is there a way you can modify the existing system to account for station closings?

Fortunately, there is, and armed with your graph search knowledge, you can step in to help out.

First up, towards the top of your code, below your landmark_string variable, create a new variable stations_under_construction and set it equal to an empty list.

36.
With certain stations closed, some routes will cease to exist. We need to account for that. Inside new_route(), wrap both shortest_route_string‘s definition and the print statement below it in an if statement that checks if shortest_route exists.

37.
Create an else condition below (but still above your definition of again). Inside, print the following:

"Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point)
38.
Nice work! It’s time for you to roll up your sleeves and create a modified version of your vc_metro graph to work with. Of course you could do this manually, but what if the list of stations under construction changes? It’s probably going to save everyone a lot of time if you just create a function that automatically generates an updated graph based on what is added to the stations_under_construction list. Ready? Define a new function called get_active_stations() without any parameters. Inside the function body, set a new variable updated_metro equal to the vc_metro dictionary.

39.
In order to create the updated system, we need to remove any connections to and from the closed stations. Create a for loop that checks each station_under_construction in stations_under_construction.

40.
Inside the for loop, create a nested for loop that checks each current_station and its corresponding neighboring_stations set from the vc_metro dictionary.


Stuck? Get a hint
41.
Inside the dictionary loop, check if current_station is NOT the station_under_construction. If it’s a station that isn’t under construction, we want to remove any of its connecting stations that are under construction. Give current_station in the updated_metro dictionary a value of its current set of stations minus a set of the stations_under_construction.

This part can be tricky, so feel free to sneak a peek at the hint for how this should look.


Stuck? Get a hint
42.
Create an else condition (this is for when the current_station is a station_under_construction). Inside, set current_station as a key in the updated_metro dictionary with a value of set([]). This will allow us to keep the current landmarks dictionary but prevent any connections from the stations that are under repair.

43.
Outside of both for loops, at the end of the get_active_stations() function, return your expertly crafted updated_metro graph.

Try adding a station name or two to the stations_under_construction list and print your call of get_active_stations() in the console.

Did you get a graph that prevents connections to and from the station(s) you added to the list?

44.
Alright! Let’s tweak get_route() so that it accommodates our new updated_metro graph if there are stations under construction.

Go back into get_route(). Inside the inner for loop, above your definition of route use a conditional expression (also known as a ternary operator) that:

sets a new variable metro_system equal to the updated metro graph returned by get_active_stations if stations_under_construction isn’t empty.
otherwise sets the variable equal to vc_metro.

Stuck? Get a hint
45.
Below this, create an if statement that checks if stations_under_construction isn’t empty. Now, before we go checking for the shortest route, let’s find out if a route even exists.

Do you remember which algorithm is helpful for this?

If you were thinking depth-first search, you remembered correctly!

46.
Inside the if condition:

Create a new variable possible_route.
Set it equal to a call of dfs() on metro_system, start_station, and end_station.
47.
Still inside the if condition, return None if there is no possible route.

Bear in mind, if we return None here, then shortest_route will be None in new_route() and we have some control flow set up to handle that condition.


Stuck? Get a hint
48.
One last step before we can test everything out! On the line where you defined route in get_route(), change vc_metro to metro_system so that we can get the shortest route for whichever metro graph is currently in place.

49.
Give yourself a pat on the back because you just created a fantastic program!

Go ahead and call skyroute() at the bottom of skyroute.py.

Save your code and in the terminal enter python3 skyroute.py to test out all of the graph search awesomeness you built out.

50.
BONUS: Add more features!

What happens if the user enters the same station for their origin and destination?
What if Vancouver’s system wants a user interface for employees to update the stations under construction?
Can you think of other ways to improve this program?

Code Editor
68696765666364616260585957


Terminal


SkyRoute: A Graph Search Program
50/50 Complete
"""

--------------------------------------------------
# "skyroute.py"
--------------------------------------------------

from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:

landmark_string=""
stations_under_construction=['Lincoln']

landmark_string = ""
for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)

def greet():
  print("Hi there and welcome to SkyRoute!\n"+"We'll help you find the shortest route between the following Vancouver landmarks:\n"+landmark_string)

def skyroute():
  greet()
  new_route()
  goodbye()

def set_start_and_end(start_point, end_point):
  if start_point:
    change_point=input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    if change_point=="b":
      start_point=get_start()
      end_point=get_end()
    elif change_point=="o":
      start_point=get_start()
    elif change_point=="d":
      end_point=get_end()
    else:
      print("Oops, that isn't 'o', 'd', or 'b'...")
      return set_start_and_end(start_point, end_point)
  else:
    start_point=get_start()
    end_point=get_end()
  return start_point, end_point

def get_start():
  start_point_letter=input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices.keys():
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_start()

def get_end():
  end_point_letter=input("Ok, where are you headed? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices.keys():
    end_point = landmark_choices[end_point_letter]
    return end_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_end()

def new_route(start_point=None, end_point=None):
  start_point, end_point = set_start_and_end(start_point, end_point)
  if start_point==end_point:
    shortest_route=["\nYou're already at your destination!\n"]
  else:
    shortest_route=get_route(start_point, end_point)
  if shortest_route:
    shortest_route_string="\n".join(shortest_route)
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
  else:
    print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))
  again=input("Would you like to see another route? Enter y/n: ")
  if again=="y":
    show_landmarks()
    return new_route(start_point, end_point)

def get_route(start_point, end_point):
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  routes=[]
  for start_station in start_stations:
    for end_station in end_stations:
      if stations_under_construction:
        metro_system=get_active_stations()
      else:
        metro_system=vc_metro
      if stations_under_construction:
        possible_route=dfs(metro_system, start_station, end_station)
        if not possible_route:
          return None
      route=bfs(metro_system,start_station,end_station)
      if route:
        routes.append(route)
  shortest_route=min(routes, key=len)
  return shortest_route

def show_landmarks():
  see_landmarks=input("Would you like to see the list of landmarks again? Enter y/n: ")
  if see_landmarks=="y":
    print(landmark_string)

def goodbye():
  print("Thanks for using SkyRoute!")

def get_active_stations():
  updated_metro=vc_metro
  for station_under_construction in stations_under_construction:
    for current_station, neighboring_stations in vc_metro.items():
      if current_station != station_under_construction:
        updated_metro[current_station]-=set(stations_under_construction)
      else:
        updated_metro[current_station]=set([])
  return updated_metro

skyroute()

#print(set_start_and_end(None, None))

#print(get_route('Marine Building','Central Park'))

#print(get_active_stations())

--------------------------------------------------
# "graph_search.py"
--------------------------------------------------

def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
	
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        if neighbor == target_value:
          return path + [neighbor]
		  
        else:
          bfs_queue.append([neighbor, path + [neighbor]])


def dfs(graph, current_vertex, target_value, visited = None):
  if visited is None:
    visited = []
	
  visited.append(current_vertex)
  
  if current_vertex == target_value:
    return visited
	
  for neighbor in graph[current_vertex]:
    if neighbor not in visited:
      path = dfs(graph, neighbor, target_value, visited)
	  
      if path:
        return path

--------------------------------------------------
# "vc_metro.py"
--------------------------------------------------

vc_metro = {
  'Richmond-Brighouse': set(['Lansdowne']),
  'Lansdowne': set(['Richmond-Brighouse', 'Aberdeen']),
  'Aberdeen': set(['Lansdowne', 'Bridgeport']),
  'Bridgeport': set(['Aberdeen', 'Templeton', 'Marine Drive']),
  'YVR-Airport': set(['Sea Island Centre']),
  'Sea Island Centre': set(['YVR-Airport', 'Templeton']),
  'Templeton': set(['Sea Island Centre', 'Bridgeport']),
  'Marine Drive': set(['Bridgeport', 'Langara-49th Avenue']),
  'Langara-49th Avenue': set(['Marine Drive', 'Oakbridge-41st Avenue']),
  'Oakbridge-41st Avenue': set(['Langara-49th Avenue', 'King Edward']),
  'King Edward': set(['Oakbridge-41st Avenue', 'Broadway-City Hall']),
  'Broadway-City Hall': set(['King Edward', 'Olympic Village']),
  'Olympic Village': set(['Broadway-City Hall', 'Yaletown-Roundhouse']),
  'Yaletown-Roundhouse': set(['Olympic Village', 'Vancouver City Centre']),
  'Vancouver City Centre': set(['Yaletown-Roundhouse', 'Waterfront']),
  'Waterfront': set(['Vancouver City Centre', 'Burrard']),
  'Burrard': set(['Waterfront', 'Granville']),
  'Granville': set(['Burrard', 'Stadium-Chinatown']),
  'Stadium-Chinatown': set(['Granville', 'Main Street-Science World']),
  'Main Street-Science World': set(['Stadium-Chinatown', 'Commercial-Broadway']),
  'Commercial-Broadway': set(['VCC-Clark', 'Main Street-Science World', 'Renfrew', 'Nanaimo']),
  'VCC-Clark': set(['Commercial-Broadway']),
  'Nanaimo': set(['Commercial-Broadway', '29th Avenue']),
  '29th Avenue': set(['Nanaimo', 'Joyce-Collingwood']),
  'Joyce-Collingwood': set(['29th Avenue', 'Patterson']),
  'Patterson': set(['Joyce-Collingwood', 'Metrotown']),
  'Metrotown': set(['Patterson', 'Royal Oak']),
  'Royal Oak': set(['Metrotown', 'Edmonds']),
  'Edmonds': set(['Royal Oak', '22nd Street']),
  '22nd Street': set(['Edmonds', 'New Westminster']),
  'New Westminster': set(['22nd Street', 'Columbia']),
  'Columbia': set(['New Westminster', 'Sapperton', 'Scott Road']),
  'Scott Road': set(['Columbia', 'Gateway']),
  'Gateway': set(['Scott Road', 'Surrey Central']),
  'Surrey Central': set(['Gateway', 'King George']),
  'King George': set(['Surrey Central']),
  'Sapperton': set(['Columbia', 'Braid']),
  'Braid': set(['Sapperton', 'Lougheed Town Centre']),
  'Lougheed Town Centre': set(['Braid', 'Production Way / University', 'Burquitlam']),
  'Burquitlam': set(['Lougheed Town Centre', 'Moody Centre']),
  'Moody Centre': set(['Burquitlam', 'Inlet Centre']),
  'Inlet Centre': set(['Moody Centre', 'Coquitlam Central']),
  'Coquitlam Central': set(['Inlet Centre', 'Lincoln']),
  'Lincoln': set(['Coquitlam Central', 'Lafarge Lake-Douglas']),
  'Lafarge Lake-Douglas': set(['Lincoln']),
  'Production Way / University': set(['Lougheed Town Centre', 'Lake City Way']),
  'Lake City Way': set(['Production Way / University', 'Sperling / Burnaby Lake']),
  'Sperling / Burnaby Lake': set(['Lake City Way', 'Holdom']),
  'Holdom': set(['Sperling / Burnaby Lake', 'Brentwood Town Centre']),
  'Brentwood Town Centre': set(['Holdom', 'Gilmore']),
  'Gilmore': set(['Brentwood Town Centre', 'Rupert']),
  'Rupert': set(['Gilmore', 'Renfrew']),
  'Renfrew': set(['Rupert', 'Commercial-Broadway'])
  }

--------------------------------------------------
# "vc_landmarks.py"
--------------------------------------------------

vc_landmarks = {
  'Marine Building': set(['Burrard', 'Waterfront']),
  'Scotiabank Field at Nat Bailey Stadium': set(['King Edward']),
  'Vancouver Aquarium': set(['Burrard']),
  'Vancouver Lookout': set(['Waterfront']),
  'Canada Place': set(['Burrard', 'Waterfront']),
  'Cathedral of Our Lady of the Holy Rosary': set(['Vancouver City Centre', 'Granville']),
  'Library Square': set(['Vancouver City Centre', 'Stadium-Chinatown']),
  'B.C. Place Stadium': set(['Stadium-Chinatown']),
  'Lions Gate Bridge': set(['Burrard']),
  'Gastown Steam Clock': set(['Waterfront']),
  'Waterfront Station': set(['Waterfront']),
  'Granville Street': set(['Granville', 'Vancouver City Centre']),
  'Pacific Central Station': set(['Main Street-Science World']),
  'Prospect Point Lighthouse': set(['Burrard']),
  'Queen Elizabeth Theatre': set(['Stadium-Chinatown']),
  'Stanley Park': set(['Burrard']),
  'Granville Island Public Market': set(['Yaletown-Roundhouse']),
  'Kitsilano Beach': set(['Olympic Village']),
  'Dr. Sun Yat-Sen Classical Chinese Garden': set(['Stadium-Chinatown']),
  'Museum of Vancouver': set(['Yaletown-Roundhouse']),
  'Science World': set(['Main Street-Science World']),
  'Robson Square': set(['Vancouver City Centre']),
  'Samson V Maritime Museum': set(['Columbia']),
  'Burnaby Lake': set(['Sperling / Burnaby Lake', 'Lake City Way', 'Production Way / University']),
  'Nikkei National Museum & Cultural Centre': set(['Edmonds']),
  'Central Park': set(['Patterson', 'Metrotown'])
}

--------------------------------------------------
# "landmark_choices.py"
--------------------------------------------------

landmark_choices = {
  'a': 'Marine Building',
  'b': 'Scotiabank Field at Nat Bailey Stadium',
  'c': 'Vancouver Aquarium',
  'd': 'Vancouver Lookout',
  'e': 'Canada Place',
  'f': 'Cathedral of Our Lady of the Holy Rosary',
  'g': 'Library Square',
  'h': 'B.C. Place Stadium',
  'i': 'Lions Gate Bridge',
  'j': 'Gastown Steam Clock',
  'k': 'Waterfront Station',
  'l': 'Granville Street',
  'm': 'Pacific Central Station',
  'n': 'Prospect Point Lighthouse',
  'o': 'Queen Elizabeth Theatre',
  'p': 'Stanley Park',
  'q': 'Granville Island Public Market',
  'r': 'Kitsilano Beach',
  's': 'Dr. Sun Yat-Sen Classical Chinese Garden',
  't': 'Museum of Vancouver',
  'u': 'Science World',
  'v': 'Robson Square',
  'w': 'Samson V Maritime Museum',
  'x': 'Burnaby Lake',
  'y': 'Nikkei National Museum & Cultural Centre',
  'z': 'Central Park'
}
