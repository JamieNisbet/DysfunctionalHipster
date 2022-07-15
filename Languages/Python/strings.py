name = 'Jamie'
age = 22

# print('Hello, my name is ' + name + ' and I am ' + str(age))
 
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# print(f'My name is {name} and I am {age}.')

s = 'hello world'

print(s.replace('world', 'everyone').upper())

print(s.split())

print('Is it alphanumeric?', s.isalnum())

print('Is it alphabetic?', s.isalpha())

print('w is in the ', s.find('w'), 'th position')

print('Is it numeric?', s.isnumeric())