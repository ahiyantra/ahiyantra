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

def convert_damages_data(damages):
  """Convert damages data from string to float and return converted data as a list."""
  conversion = {"M": 1000000,
               "B": 1000000000}

  updated_damages = list()
  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    if damage.find('M') != -1:
      updated_damages.append(float(damage[0:damage.find('M')])*conversion["M"])
    if damage.find('B') != -1:
      updated_damages.append(float(damage[0:damage.find('B')])*conversion["B"])
  return updated_damages

# update damages data
updated_damages = convert_damages_data(damages)

def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  """Create dictionary of hurricanes with hurricane name as the key and a dictionary of hurricane data as the value."""
  hurricanes = dict()
  num_hurricanes = len(names)
  for i in range(num_hurricanes):
    hurricanes[names[i]] = {"Name": names[i],
                          "Month": months[i],
                          "Year": years[i],
                          "Max Sustained Wind": max_sustained_winds[i],
                          "Areas Affected": areas_affected[i],
                          "Damage": updated_damages[i],
                          "Deaths": deaths[i]}
  return hurricanes

# create hurricanes dictionary
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

def create_year_dictionary(hurricanes):
  """Convert dictionary with hurricane name as key to a new dictionary with hurricane year as the key and return new dictionary."""
  hurricanes_by_year= dict()
  for cane in hurricanes:
      current_year = hurricanes[cane]['Year']
      current_cane = hurricanes[cane]
      if current_year not in hurricanes_by_year:
          hurricanes_by_year[current_year] = [current_cane]
      else:
          hurricanes_by_year[current_year].append(current_cane)
  return hurricanes_by_year

# create a new dictionary of hurricanes with year and key
hurricanes_by_year = create_year_dictionary(hurricanes)
print(hurricanes_by_year[1932])

def count_affected_areas(hurricanes):
  """Find the count of affected areas across all hurricanes and return as a dictionary with the affected areas as keys."""
  affected_areas_count = dict()
  for cane in hurricanes:
    for area in hurricanes[cane]['Areas Affected']:
      if area not in affected_areas_count:
        affected_areas_count[area] = 1
      else:
        affected_areas_count[area] += 1
  return affected_areas_count

# create dictionary of areas to store the number of hurricanes involved in
affected_areas_count = count_affected_areas(hurricanes)

def most_affected_area(affected_areas_count):
  """Find most affected area and the number of hurricanes it was involved in."""
  max_area = 'Central America'
  max_area_count = 0
  for area in affected_areas_count:
    if affected_areas_count[area] > max_area_count:
      max_area = area
      max_area_count = affected_areas_count[area]
  return max_area, max_area_count

# find most frequently affected area and the number of hurricanes involved in
max_area, max_area_count = most_affected_area(affected_areas_count)
print(max_area,max_area_count)

def highest_mortality(hurricanes):
  """Find the highest mortality hurricane and the number of deaths it caused."""
  max_mortality_cane = 'Cuba I'
  max_mortality = 0
  for cane in hurricanes:
    if hurricanes[cane]['Deaths'] > max_mortality:
      max_mortality_cane = cane
      max_mortality = hurricanes[cane]['Deaths']
  return max_mortality_cane, max_mortality

# find highest mortality hurricane and the number of deaths
max_mortality_cane, max_mortality = highest_mortality(hurricanes)
print(max_mortality_cane, max_mortality)

def categorize_by_mortality(hurricanes):
  """Categorize hurricanes by mortality and return a dictionary."""
  mortality_scale = {0: 0,
                 1: 100,
                 2: 500,
                 3: 1000,
                 4: 10000}
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricanes:
    num_deaths = hurricanes[cane]['Deaths']
    if num_deaths == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricanes[cane])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricanes[cane])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricanes[cane])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricanes[cane])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricanes[cane])
    elif num_deaths > mortality_scale[4]:
      hurricanes_by_mortality[5].append(hurricanes[cane])
  return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = categorize_by_mortality(hurricanes)
print(hurricanes_by_mortality[5])

def highest_damage(hurricanes):
  """Find the highest damage inducing hurricane and its total cost."""
  max_damage_cane = 'Cuba I'
  max_damage = 0
  for cane in hurricanes:
    if hurricanes[cane]['Damage'] == "Damages not recorded":
      pass
    elif hurricanes[cane]['Damage'] > max_damage:
      max_damage_cane = cane
      max_damage = hurricanes[cane]['Damage']
  return max_damage_cane, max_damage

# find highest damage inducing hurricane and its total cost
max_damage_cane, max_damage = highest_damage(hurricanes)
print(max_damage_cane, max_damage)

def categorize_by_damage(hurricanes):
  """Categorize hurricanes by damage and return a dictionary."""
  damage_scale = {0: 0,
                 1: 100000000,
                 2: 1000000000,
                 3: 10000000000,
                 4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricanes:
    total_damage = hurricanes[cane]['Damage']
    if total_damage == "Damages not recorded":
      hurricanes_by_damage[0].append(hurricanes[cane])
    elif total_damage == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricanes[cane])
    elif total_damage > damage_scale[0] and total_damage <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes[cane])
    elif total_damage > damage_scale[1] and total_damage <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes[cane])
    elif total_damage > damage_scale[2] and total_damage <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes[cane])
    elif total_damage > damage_scale[3] and total_damage <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes[cane])
    elif total_damage > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricanes[cane])
  return hurricanes_by_damage

# categorize hurricanes in new dictionary with damage severity as key
hurricanes_by_damage = categorize_by_damage(hurricanes)
print(hurricanes_by_damage[5])
