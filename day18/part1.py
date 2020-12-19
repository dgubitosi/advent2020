
import sys

DIGITS = '0123456789'
OPERATORS = '+*'

def calculate(left, right, operation):
    print(left, operation, right)
    if operation == '+':
        temp = int(left) + int(right)
    if operation == '*':
        temp = int(left) * int(right)
    return str(temp)

def solve(expression):
    print(expression)
    left = ''
    right = ''
    operation = None
    while expression:
        c = expression[0]
        expression = expression[1:]
        if DIGITS.find(c) > -1:
            if not operation:
                left += c
            else:
                right += c
        if OPERATORS.find(c) > -1:
            if operation:
                left = calculate(left, right, operation)
                right = ''
                operation = None
            operation = c
    # do the last calculation
    if right:
        left = calculate(left, right, operation)
    return str(left)

def resolve_parens(expression):
    while True:
        # find the first closed parens
        closed = expression.find(')')
        if closed != -1:
            # reverse find the nearest open parens to it
            opened = expression.rfind('(', 0, closed)
            # calculate the intermediate expression
            expression = expression[0:opened] + solve(expression[opened+1:closed]) + expression[closed+1:]
            print(expression)
        # no more parens to resolve
        else: break
    return int(solve(expression))

total = 0
with open(sys.argv[1]) as f:
    for line in f:
        expression = line.strip()
        expression = expression.replace(' ',  '')
        print(expression)
        total += resolve_parens(expression)
print(total)