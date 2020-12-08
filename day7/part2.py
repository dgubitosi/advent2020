
import sys

bags = dict()
with open(sys.argv[1]) as f:
    for line in f:
        bag, line = line.strip().split(' bags contain')
        contents = line.split(',')
        for c in contents:
            c = c.strip()
            if c.startswith('no other'):
                bags[bag] = None
            else:
                words = c.split()
                number = int(words[0])
                name = ' '.join(words[1:-1])
                bags.setdefault(bag, dict())
                bags[bag].setdefault(name, dict())
                bags[bag][name] = number

total = 0
shiny = 'shiny gold'
toResolve = [ { shiny:1 } ]
while toResolve:
    p = toResolve.pop()
    print(p)
    k = list(p)
    assert len(k) == 1
    parent = k[0]
    quantity = p[k[0]]
    children = bags[parent]
    if not children: continue
    for child in children:
        q = bags[parent][child]
        q *= quantity
        total += q
        c = { child: q }
        toResolve.append(c)
print(total)