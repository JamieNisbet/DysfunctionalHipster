person = {
    'first_name': 'Jamie',
    'last_name': 'Nisbet',
    'age': 22
}

print(person['first_name'])
print(person.get('last_name'))

person['phone'] = '555-555-5555'

# print(person.keys())

# person2 = person.copy()
# person2['city'] = 'Boston'

# del(person2['age'])
# person2.pop('phone')

# person.clear()

# print(person2)
print(person)

people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)