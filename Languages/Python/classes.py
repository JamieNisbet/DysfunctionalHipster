class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
        

jamie = User('Jamie Nisbet', 'jamie@me.com', 22)
louis = Customer('Louis', 'louis@me.com', 25)

louis.set_balance(500)
print(louis.greeting())

print(jamie.email)
