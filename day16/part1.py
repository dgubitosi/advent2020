
import sys

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


print(rules)
print(my_ticket)
print(tickets)