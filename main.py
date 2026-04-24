from logo import logo

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

def calculator():
    print(logo)
    should_continue = True
    a = float(input('Pick a number: '))
    while should_continue:
        for key in operations:
            print(key)
        op = input('What operation do you want to proceed?: ')
        if op not in operations:
            print("Invalid operation. Try again.")
            continue
        b = float(input('Pick the second number: '))
        if b == 0 and op in ['/', '//', '%']:
            print("You can't do that operation with 0.")
            continue

        result = operations[op](a, b)
        print(f'{a} {op} {b} = {result}')

        choice = input(f'Do you want to continue calculation with {result} ? Type y/n:  ')

        if choice == 'y':
            a = result
        else:
            should_continue = False
            print('\n' * 5)

    restart = input('Do you want to start a new calculation ? y/n: ')
    if restart == 'y':
        calculator()
    else:
        print('Thanks for using the calculator.')

calculator()