
import sys

adapters = []
with open(sys.argv[1]) as f:
    adapters = [ int(x.strip()) for x in f.readlines() ]

adapters.sort()
adapters.insert(0, 0)
device = adapters[-1] + 3
adapters.append(device)

delta = dict()
for i in range(1, len(adapters)):
    d = adapters[i] - adapters[i-1]
    delta.setdefault(d, 0)
    delta[d] += 1

for d in sorted(delta):
    print(d, delta[d])

print(delta[1]*delta[3])
