
import sys

def validate(ticket):

    errors = 0
    for t in ticket:
        valid = False
        for r in rules:
            if valid: break
            #print(rule)
            for values in rules[r]:
                #print(t, r)
                if int(values[0]) <= int(t) <= int(values[-1]): valid = True
                if valid: break
        if not valid: errors += int(t)
    return errors

rules = dict()
tickets = list()
my_ticket = list()

mine = False
nearby = False
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if nearby:
            tickets.append(line.split(','))
            continue
        if line.find(' or ') != -1:
            name, v = line.split(': ')
            values = v.split(' or ')
            rules.setdefault(name, list())
            for v in values:
                rules[name].append(tuple(v.split('-')))
            continue
        if line.find('your') != -1:
            mine = True
            continue
        if mine:
            my_ticket = line.split(',')
            mine = False
            continue
        if line.find('nearby') != -1:
            nearby = True
            continue

#print(rules)
#print(my_ticket)
#print(tickets)

error_rate = 0
for t in tickets:
    error_rate += validate(t)
print(error_rate)

