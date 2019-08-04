# Nesting
# dictinoaries can have lists, dictionaries as values
person1 = {'name':'john', 'places': ['Barcelona', 'New York', 'London']}
# print(person1['places']) # this will print as list 
# first_place = person1['places'] [0]
# print(first_place)

for place in person1['places']:
    print(f'{place} is the favourite place. ')

# values as dictionaries 

person1 = {'name': 'khabib', 'location': 'Brooklyn', 'gender': 'male'}
person2 = {'name': 'rustam', 'location': 'new jersey', 'gender': 'male'}
person3 = {'name': 'roza', 'location': 'paris', 'gender': 'female'}

# people= [] # this is the list
# people.append(person1)
# people.append(person2)
# people.append(person3)
# print(f"{people[0]['name']}'s in {people[0]['location']} city. ")

#values in dictionary are dictionaries 
# people_dict = {}
# people_dict['person1'] = person1 # adding dictionary object in people dictionary 
# people_dict['person2'] = person2
# people_dict['person3'] = person3
# print(people_dict)

# # rustam`s location
# print(people_dict['person2']['location'].title())
# print(len(people_dict)) # length of the dictionasry, count of object in it 

bunny = {'name' : 'bunny', 'type' : 'rabbit', 'owner': 'Mark'}
rex = {'name' : 'rex', 'type' : 'dog', 'owner': ' roza'}
gosha = {'name' : 'gosha', 'type' : 'cow', 'owner': 'misha'}

pets = []
pets.append(bunny)
pets.append(rex)
# pets = [rex, bunny, gosha] alternative to above 3 lines
pets.append(gosha)
print(pets)

for pet in pets:
    print(pet)

pets = {}
pets