import json

userJSON = '{"firstname": "Jamie", "lastname": "Nisbet", "age": 22}'
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

user = json.loads(userJSON)
carJSON = json.dumps(car)

print('This is in Python dictionnary format =>', user)
print('This is in JSON format =>', carJSON)