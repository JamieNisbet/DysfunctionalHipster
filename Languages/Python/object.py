import json

items = json.loads('[{"id":1, "text": "Hello"}, {"id":2, "text":"World"}, {"id":3, "text":"This works"}]')

for item in items:
    print(item['text'])  

# This file takes JSON as input, transfers it to a python object and prints it out