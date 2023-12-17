
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"];

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']];

def get_destination_index(destination):
  for n in range(len(destinations)):
    if destination == destinations[n]:
      destination_index = n;
  return destination_index;

#test0 = get_destination_index("Los Angeles, USA");
#print(test0);

#test0 = get_destination_index("Paris, France");
#print(test0);

#test0 = get_destination_index("Hyderabad, India");
#print(test0);

def get_traveler_location(traveler):
  traveler_destination = traveler[1];
  traveler_destination_index = get_destination_index(traveler_destination);
  return traveler_destination_index;

#test_destination_index = get_traveler_location(test_traveler);
#print(test_destination_index);

attractions = [list() for x in range(0,5)];
#print(attractions);

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination);
  except ValueError:
    print("The chosen destination isn't available!")
    return;
  except:
    print("Something's wrong!")
    return;
  attractions_for_destination = attractions[destination_index];
  attractions_for_destination.append(attraction);

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']]);
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]]);
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]]);
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]]);
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]]);
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]]);
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]]);
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]]);
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]]);
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]]);
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]]);
#print(attractions);

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination);
  attractions_in_city = attractions[destination_index];
  attractions_with_interest = [];
  attraction_tags = [];
  
  for ac in attractions_in_city:
    possible_attraction = ac;
    for ar in range(0, len(ac[1])):
      attraction_tags.append(ac[1][ar]);
  if type(interests) != type(attraction_tags):
    listed_interests = [];
    listed_interests.append(interests);
    interests = listed_interests;
  
  for ac in attractions_in_city:
    possible_attraction = ac;
    for i in interests:
      for t in attraction_tags:
        if i == t:
          possible_attraction_tags = possible_attraction[1];
          poatta = [];
          if type(poatta) != type(possible_attraction_tags):
            poatta.append(possible_attraction_tags);
          if type(poatta) == type(possible_attraction_tags):
            poatta = possible_attraction_tags;
          for n in poatta:
            if i == n:
              attractions_with_interest.append(possible_attraction[0]);
  
  return attractions_with_interest;

#la_arts = find_attractions("Los Angeles, USA", "art");
#print(la_arts);

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1];
  traveler_interests = traveler[2];
  traveler_attractions = find_attractions(traveler_destination, traveler_interests);
  print("");
  interests_string = "Hi ";
  interests_string = interests_string + traveler[0];
  interests_string = interests_string + ", we think you'll like these places around " + traveler_destination + ": ";
  for ta in traveler_attractions:
    interests_string = interests_string + ta + ", ";
  interests_string = interests_string + "et cetera.";
  return interests_string;

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]);
print(smills_france);
borjigins_brazil = get_attractions_for_traveler(['Temujin Borjigin', 'São Paulo, Brazil', ['zoo', 'historical site']]);
print(borjigins_brazil);
test_travelers_tour = get_attractions_for_traveler(test_traveler);
print(test_travelers_tour);
