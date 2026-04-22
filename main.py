def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def power(a,b):
    return a ** b

def modulo(a,b):
    return a % b

def floor_div(a,b):
    return a // b

op = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '%': modulo,
    '//': floor_div,
}

a = int(input('Pick a number: '))
for key in op:
    print(key)
what = input('What operation do you want to proceed?: ')
b = int(input('Pick the second number: '))

result = op[what](a,b)
print(result)
