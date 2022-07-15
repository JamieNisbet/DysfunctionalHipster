def sayHello(name = 'Sam'):
    print (f'Hello {name}')

sayHello()

# def getSum(num1, num2):
#     total = num1 + num2
#     return total

# sum = getSum(3, 4)

# print(sum)

getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 3)) 