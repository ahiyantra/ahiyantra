
def contains(big_string, little_string):
  v = False;
  for l0 in range(0, len(big_string)-1):
    if little_string[0] == big_string[l0]:
      if len(big_string) > l0+len(little_string)-1:
        if  little_string[-1] == big_string[l0+len(little_string)-1]:
          v = True;
  return v;

def common_letters (string_one, string_two):
  n = [];
  for l0 in string_one:
    for l1 in string_two:
      if l0 == l1:
        if len(n) == 0:
          n.append(l0);
        elif len(n) == 1:
          if n[0] != l0:
            n.append(l0);
        elif len(n) == 2:
          if n[1] != l0:
            if n[0] != l0:
              n.append(l0);
  return n;

def username_generator(first_name, last_name):
  a = ""; b = "";
  if len(first_name) > 3:
    a = first_name[0:3];
  else:
    a = first_name;
  if len(last_name) > 4:
    b = last_name[0:4];
  else:
    b = last_name;
  username = a + b;
  return username;

def password_generator(username):
  password = "";
  for u in range(0, len(username)):
    password = password + username[u-1];
  return password;

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    '];

love_maybe_lines_stripped = [];

for n in range(0, len(love_maybe_lines)):
  love_maybe_lines_stripped.append(love_maybe_lines[n].strip());

love_maybe_full = '\n'.join(love_maybe_lines_stripped);

print(love_maybe_full);

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')

def poem_title_card(poet, title):
  return "The poem \"{}\" is written by {}.".format(title, poet);

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

print(highlighted_poems_list)

highlighted_poems_stripped = []

for n in range(0, len(highlighted_poems_list)):
  highlighted_poems_stripped.append(highlighted_poems_list[n].strip());

print(highlighted_poems_stripped)

highlighted_poems_details = []

for n in range(0, len(highlighted_poems_stripped)):
  highlighted_poems_details.append(highlighted_poems_stripped[n].split(':'));

titles = []
poets = []
dates = []

print(highlighted_poems_details)

for n in range(0, len(highlighted_poems_details)):
  titles.append(highlighted_poems_details[n][0]);
  poets.append(highlighted_poems_details[n][1]);
  dates.append(highlighted_poems_details[n][-1]);

for n in range(0, len(highlighted_poems_details)):
  print("The poem {} was published by {} in {}.".format(titles[n], poets[n], dates[n]))

when_you_are_old = \
"""When you are old and grey and full of sleep,
And nodding by the fire, take down this book,
And slowly read, and dream of the soft look
Your eyes had once, and of their shadows deep;

How many loved your moments of glad grace,
And loved your beauty with love false or true,
But one man loved the pilgrim soul in you,
And loved the sorrows of your changing face;

And bending down beside the glowing bars,
Murmur, a little sadly, how Love fled
And paced upon the mountains overhead
And hid his face amid a crowd of stars."""

# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1, 100) for x in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random

# Add your code below:

numbers_a = range(1, 13)
numbers_b = [random.randint(1, 1000) for x in range(12)]
plt.plot(numbers_a, numbers_b)
plt.show()

cost_of_gum = 0.10
cost_of_gumdrop = 0.35

cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.44999999999999996

from decimal import Decimal

cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.45 instead of 0.44999999999999996

# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
# Add your insert_beginning and stringify_list methods below:

  def insert_beginning(self, new_value):
    new_node=Node(new_value);
    new_node.set_next_node(self.head_node);
    self.head_node = new_node;
  def stringify_list(self):
    v0 = self.head_node;
    v1 = str(v0.get_value())+"\n";
    while v0.get_next_node() != None:
      v0 = v0.get_next_node();
      v1 = v1+str(v0.get_value())+"\n";
    return v1;

# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())

# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  # Define your remove_node method below:
  def remove_node(self, value_to_remove):
    self.value_to_remove=value_to_remove;
    current_node=self.head_node;
    if current_node.get_value()==self.value_to_remove:
      self.head_node = current_node.get_next_node();
    else:
      while current_node.get_next_node() != None:
        if current_node.get_next_node().get_value() == self.value_to_remove:
          current_node.set_next_node(current_node.next_node.get_next_node());
          #current_node=None;
        current_node = current_node.get_next_node();

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
----------------------------------------------------------------------------------------------------------
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    """
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]
    
    if current_array_value != None:
      if current_array_value[0] == key:
        self.array[array_index] = [key, value]
    else:
      self.array[array_index] = [key, value]
    """
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return
      """
    # current_array_value currently holds different key
    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]
    if possible_return_value == None:
      return None
    else:
      if possible_return_value[0] == key:
        return possible_return_value[1]
----------------------------------------------------------------------------------------------------------
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    """
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return
    else:
      number_collisions = 1
      while current_array_value[0] != key:
        new_hash_code = self.hash(key, number_collisions)
        new_array_index = self.compressor(new_hash_code)
        current_array_value = self.array[new_array_index]
        if current_array_value is None:
          self.array[new_array_index] = [key, value]
          return
        if current_array_value[0] == key:
          self.array[new_array_index] = [key, value]
          return
        else:
          number_collisions += 1

    # current_array_value currently holds different key
    return
    """
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision!

    number_collisions = 1

    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return
    """
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
        return None

    if possible_return_value[0] == key:
        return possible_return_value[1]

    # possible_return_value holds different key
    return
----------------------------------------------------------------------------------------------------------
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision!

    number_collisions = 1

    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return

  def retrieve(self, key):
    """
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
        return None

    if possible_return_value[0] == key:
        return possible_return_value[1]
    else:
      retrieval_collisions = 1
      while possible_return_value[0] != key:
        new_hash_code = self.hash(key, retrieval_collisions)
        retrieving_array_index = self.compressor(new_hash_code)
        possible_return_value = self.array[retrieving_array_index]
        if possible_return_value == None:
          return None
        if possible_return_value[0] != key:
          retrieval_collisions += 1
        else:
          return possible_return_value[1]
    # possible_return_value holds different key
    return
    """
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
      return None

    if possible_return_value[0] == key:
      return possible_return_value[1]

    retrieval_collisions = 1

    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return
    """