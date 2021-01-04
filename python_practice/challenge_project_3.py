"""

Hurricane Analysis

Avatar
Hurricane AnalysisBrief
Objective
Hurricane Analysis
Overview
This project is slightly different than others you have encountered thus far on Codecademy. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you’ll be building. There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

Project Goals
You will work to write several functions that organize and manipulate data about Category 5 Hurricanes, the strongest hurricanes as rated by their wind speed. Each one of these functions will use a number of parameters, conditionals, lists, dictionaries, string manipulation, and return statements.

Setup Instructions
If you choose to do this project on your computer instead of Codecademy, you can download what you’ll need by clicking the “Download” button below. If you need help setting up your computer, be sure to check out our setup guide.

Tasks
11/11 Complete
Mark the tasks as complete by checking them off
Prerequisites
1.
In order to complete this project, you should have completed the Loops and Dictionaries sections of the Learn Python 3 Course. This content is also covered in the Data Scientist Career Path.

Project Requirements
2.
Hurricanes, also known as cyclones or typhoons, are one of the most powerful forces of nature on Earth. Due to climate change caused by human activity, the number and intensity of hurricanes has risen, calling for better preparation by the many communities that are devastated by them. As a concerned environmentalist, you want to look at data about the most powerful hurricanes that have occurred.

Begin by looking at the damages list. The list contains strings representing the total cost in USD($) caused by 34 category 5 hurricanes (wind speeds ≥ 157 mph (252 km/h )) in the Atlantic region. For some of the hurricanes, damage data was not recorded ("Damages not recorded"), while the rest are written in the format "Prefix-B/M", where B stands for billions (1000000000) and M stands for millions (1000000).

Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded".

Test your function with the data stored in damages.


Stuck? Get a hint
3.
Additional data collected on the 34 strongest Atlantic hurricanes are provided in a series of lists. The data includes:

names: names of the hurricanes
months: months in which the hurricanes occurred
years: years in which the hurricanes occurred
max_sustained_winds: maximum sustained winds (miles per hour) of the hurricanes
areas_affected: list of different areas affected by each of the hurricanes
deaths: total number of deaths caused by each of the hurricanes
The data is organized such that the data at each index, from 0 to 33, corresponds to the same hurricane.

For example, names[0] yields the “Cuba I” hurricane, which ouccred in months[0] (October) years[0] (1924).

Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.

Thus the key "Cuba I" would have the value: {'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}.

Test your function on the lists of data provided.


Stuck? Get a hint
4.
In addition to organizing the hurricanes in a dictionary with names as the key, you want to be able to organize the hurricanes by year.

Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.

For example, the key 1932 would yield the value: [{'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max Sustained Wind': 160, 'Areas Affected': ['The Bahamas', 'Northeastern United States'], 'Damage': 'Damages not recorded', 'Deaths': 16}, {'Name': 'Cuba II', 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 'Areas Affected': ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}].

Test your function on your hurricane dictionary.


Stuck? Get a hint
5.
You believe that knowing how often each of the areas of the Atlantic are affected by these strong hurricanes is important for making preparations for future hurricanes.

Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.

Test your function on your hurricane dictionary.


Stuck? Get a hint
6.
Write a function that finds the area affected by the most hurricanes, and how often it was hit.

Test your function on your affected area dictionary.


Stuck? Get a hint
7.
Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.

Test your function on your hurricane dictionary.


Stuck? Get a hint
8.
Just as hurricanes are rated by their windspeed, you want to try rating hurricanes based on other metrics.

Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating.

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
For example, a hurricane with a 1 mortality rating would have resulted in greater than 0 but less than or equal to 100 deaths. A hurricane with a 5 mortality rating would have resulted in greater than 10000 deaths.

Store the hurricanes in a new dictionary where the keys are mortality ratings and the values are lists containing a dictionary for each hurricane that falls into that mortality rating.

Test your function on your hurricane dictionary.


Stuck? Get a hint
9.
Write a function that finds the hurricane that caused the greatest damage, and how costly it was.

Test your function on your hurricane dictionary.


Stuck? Get a hint
10.
Lastly, you want to rate hurricanes according to how much damage they cause.

Write a function that rates hurricanes on a damage scale according to the following ratings, where the key is the rating and the value is the upper bound of damage for that rating.

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
For example, a hurricane with a 1 damage rating would have resulted in damages greater than 0 USD but less than or equal to 100000000 USD. A hurricane with a 5 damage rating would have resulted in damages greater than 50000000000 USD (talk about a lot of money).

Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a dictionary for each hurricane that falls into that damage rating.

Test your function on your hurricane dictionary.


Stuck? Get a hint
Solution
11.
Great work! Visit our forums to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that’s okay! There are multiple ways to solve these projects, and you’ll learn more by seeing others’ code.

Code Editor
191192193194195196197198199200201202203204205206207208209


Output-only Terminal
Output:


Hurricane Analysis
11/11 Complete

"""

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def ud(d0):
  p0 = []; p1 = 0; p2 = "";
  for v0 in d0:
    if v0 != "Damages not recorded":
      #print(v0[0:(len(v0)-1)]);
      p1 = float(v0[0:(len(v0)-1)]); p2 = v0[-1];
      if p2 == "M":
        p0.append(p1*1000000);
      else:
        p0.append(p1*1000000000);
    else:
      p0.append("Damages not recorded");
  #print(p0);
  return p0;

damages = ud(damages);

# write your construct hurricane dictionary function here:

def chd(n, m, y, msw, aa, ud, d):
  p0 = {};
  for v0 in range(0, len(n)):
    p0[n[v0]] = {"Name": n[v0], "Month": m[v0], "Year": y[v0], "Max Sustained Wind": msw[v0], "Areas Affected": aa[v0], "Damage": ud[v0], "Deaths": d[v0]};
  #print(p0);
  return p0;

h_names = chd(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

# write your construct hurricane by year dictionary function here:

def chby(v0, y):
  p0 = {};
  for v1 in range(0, len(y)):
    p1 = [];
    for v2 in v0:
      if y[v1] == v0[v2]['Year']:
        p1.append(v0[v2]);
    p0[y[v1]] = p1; 
  #print(p0);
  return p0;

h_years = chby(h_names, years);

# write your count affected areas function here:

def caa(v0):
  p0 = {};
  for v1 in v0:
    for v2 in v0[v1]['Areas Affected']:
      if p0.get(v2, 0) == 0:
        p0[v2] = 1;
      else:
        p0[v2] += 1;
  #print(p0);
  return p0;

h_areas = caa(h_names);

# write your find most affected area function here:

def maa(v0):
  p0 = 0; p1 = "";p2 = {};
  for v1 in v0:
    if v0[v1]>p0:
      p0 = v0[v1];
      p1 = v1;
  p2[p1] = p0;
  print(p2);
  return p2;

h_maa = maa(h_areas);

# write your greatest number of deaths function here:

def gnod(v0):
  p0 = 0; p1 = "";p2 = {};
  for v1 in v0:
    if v0[v1]['Deaths'] > p0:
      p0 = v0[v1]['Deaths'];
      p1 = v0[v1]['Name']
  p2[p1] = p0;
  print(p2);
  return p2;

h_gnod = gnod(h_names);

# write your catgeorize by mortality function here:

def cbm(v0):
  ms = {0: 0,
        1: 100,
        2: 500,
        3: 1000,
        4: 10000,
        5: 100000,
        6: 1000000,
        7: 10000000};
  p0 = {}; p1 = []; p2 = []; p3 = []; p4 = []; p5 = []; p6 = []; p7 = []; p8 = [];
  for v1 in v0:
    if v0[v1]['Deaths'] == 0:
      p1.append(v0[v1]);
    elif v0[v1]['Deaths'] < 100:
      p2.append(v0[v1]);
    elif v0[v1]['Deaths'] < 500:
      p3.append(v0[v1]);
    elif v0[v1]['Deaths'] < 1000:
      p4.append(v0[v1]);
    elif v0[v1]['Deaths'] < 10000:
      p5.append(v0[v1]);
    elif v0[v1]['Deaths'] < 100000:
      p6.append(v0[v1]);
    elif v0[v1]['Damage'] < 1000000:
      p7.append(v0[v1]);
    elif v0[v1]['Damage'] < 10000000:
      p8.append(v0[v1]);
    p0[0] = p1;
    p0[1] = p2;
    p0[2] = p3;
    p0[3] = p4;
    p0[4] = p5;
    p0[5] = p6;
    p0[6] = p7;
    p0[7] = p8;
  #print(p0);
  return p0;

h_cbm = cbm(h_names);

# write your greatest damage function here:

def gd(v0):
  p0 = 0; p1 = "";p2 = {};
  for v1 in v0:
    if v0[v1]['Damage'] != "Damages not recorded":
      if v0[v1]['Damage'] > p0:
        p0 = v0[v1]['Damage'];
        p1 = v0[v1]['Name']
  p2[p1] = p0;
  print(p2);
  return p2;

h_gd = gd(h_names);

# write your catgeorize by damage function here:

def cbd(v0):
  ds = {0: 0,
        1: 100000000,
        2: 1000000000,
        3: 10000000000,
        4: 50000000000,
        5: 100000000000,
        6: 1000000000000,
        7: 10000000000000};
  p0 = {}; p1 = []; p2 = []; p3 = []; p4 = []; p5 = []; p6 = []; p7 = []; p8 = [];
  for v1 in v0:
    if v0[v1]['Damage'] != "Damages not recorded":
      if v0[v1]['Damage'] == 0:
        p1.append(v0[v1]);
      elif v0[v1]['Damage'] < 100000000:
        p2.append(v0[v1]);
      elif v0[v1]['Damage'] < 1000000000:
        p3.append(v0[v1]);
      elif v0[v1]['Damage'] < 10000000000:
        p4.append(v0[v1]);
      elif v0[v1]['Damage'] < 50000000000:
        p5.append(v0[v1]);
      elif v0[v1]['Damage'] < 100000000000:
        p6.append(v0[v1]);
      elif v0[v1]['Damage'] < 1000000000000:
        p7.append(v0[v1]);
      elif v0[v1]['Damage'] < 10000000000000:
        p8.append(v0[v1]);
    p0[0] = p1;
    p0[1] = p2;
    p0[2] = p3;
    p0[3] = p4;
    p0[4] = p5;
    p0[5] = p6;
    p0[6] = p7;
    p0[7] = p8;
  #print(p0);
  return p0;

h_cbd = cbd(h_names);
