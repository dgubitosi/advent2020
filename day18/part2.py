
import sys

def solve(expression):
    print(expression)
    multiply = expression.split('*')
    total = 1
    while multiply:
        addition = [ int(x) for x in multiply.pop(0).split('+') ]
        total *= sum(addition)
    return str(total)

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