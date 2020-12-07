
import sys

def walk(obj):
    paths = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = str(k)
            paths.append([p])
            paths += [ [p] + x for x in walk(bags[k]) ]
    if obj is None:
        paths.append([obj])
    return paths

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

shiny = 'shiny gold'
top = set()
paths = walk(bags)
for p in paths:
    if p[0] == shiny:
        continue
    if p[-1] is not None:
        continue
    if shiny in p:
        top.add(p[0])
print(len(top))
