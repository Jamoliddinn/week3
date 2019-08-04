# dictinaries go by Key and Value pair
# person1 = {'name': 'John', 'age':30} 
# print(person1['name']) # accessing the values by keys
# print(person1)

# # adding object to the dictionary 
# person1['occupation'] = 'QA'
# person1['is single'] = False

# print(person1)

person2 = {}
person2['name'] = 'Jamol'
person2['age'] = 25  #int(input('enter your age of person2: '))
person2['Status'] = 'married'
person2['Occupation'] = 'Lead of QA'
person2['is single'] = False
print(person2)

person2['age'] = person2['age'] + 1 # this is the same as >> person2['age'] += 1
person2['occapation'] = 'Sr. QA'
person2['location'] = 'Brooklyn'
print(person2)

del person2['location'] # this deletes the key/value pair from the person2 dictionary
print(person2)
print(person2['name'].upper())