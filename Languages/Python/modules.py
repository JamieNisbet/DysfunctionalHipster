# import datetime
# from datetime import date
# import time

# today1 = datetime.date.today()
# today2 = date.today()
# timestamp = time.time()

# print(today1)
# print(today2)

# print(timestamp)

# from camelcase import CamelCase

# c = CamelCase()

# print(c.hump('hello there world'))

import validator # validator.py

name = 'Jamie Nisbet'
name2 = 'Bob Jacobs'

validator.validate(name) 
validator.validate(name2)
