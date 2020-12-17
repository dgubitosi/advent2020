
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
                if values[0] <= t <= values[-1]: valid = True
                if valid: break
        if not valid: errors += t
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
            t = [ int(x) for x in line.split(',') ]
            # discard the bad tickets
            if validate(t) == 0:
                tickets.append(t)
            continue
        if line.find(' or ') != -1:
            name, v = line.split(': ')
            values = v.split(' or ')
            rules.setdefault(name, list())
            for v in values:
                t = [ int(x) for x in v.split('-') ]
                rules[name].append(tuple(t))
            continue
        if line.find('your') != -1:
            mine = True
            continue
        if mine:
            my_ticket = [ int(x) for x in line.split(',') ]
            mine = False
            continue
        if line.find('nearby') != -1:
            nearby = True
            continue

#print(rules)
#print(my_ticket)
#print(tickets)

found = dict()
while rules:
    for i in range(len(my_ticket)):
        invalid_rules = set()
        for r in rules:
            for row in range(len(tickets)):
                if rules[r][0][1] < tickets[row][i] < rules[r][1][0]:
                    invalid_rules.add(r)
                    break
        difference = set(rules).difference(invalid_rules) 
        #print(i, my_ticket[i], difference)
        if len(difference) == 1:
            r = difference.pop()
            #print("FOUND", i, r)
            found.setdefault(r, i)
            del rules[r]

total = 1
for f in sorted(found):
    print(f, my_ticket[found[f]])
    if f.startswith('departure'):
        total *= my_ticket[found[f]]
print()
print("departure total:", total)
