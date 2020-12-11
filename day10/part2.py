
import sys

adapters = []
with open(sys.argv[1]) as f:
    adapters = [ int(x.strip()) for x in f.readlines() ]

adapters.sort()
adapters.insert(0, 0)
device = adapters[-1] + 3
adapters.append(device)

c = list()
c.extend(adapters)

configurations = set()
toResolve = set()
toResolve.add(tuple(c))
while toResolve:
    array = list(toResolve.pop())
    if tuple(array) in configurations:
        continue
    else:
        configurations.add(tuple(array))
    i = 2
    while i < len(array):
        d = array[i] - array[i-2]
        if d <= 3:
            c = list()
            c.extend(array)
            c.pop(i-1)
            toResolve.add(tuple(c))
        i += 1

print(len(configurations))
for i, c in enumerate(list(configurations)):
    print(i+1, c)
