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

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '%': modulo,
    '//': floor_div,
}

should_continue = True
a = int(input('Pick a number: '))
while should_continue:
    for key in operations:
        print(key)
    op = input('What operation do you want to proceed?: ')
    b = int(input('Pick the second number: '))
    result = operations[op](a, b)
    print(f'{a} {op} {b} = {result}')

    choice = input(f'Type "y" to continue calculation with {result}, or type "n" to start a new calculation: ')

    if choice == 'y':
        a = result
    else:
        should_continue = False
