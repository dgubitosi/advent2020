
import sys
import math

# how can i use the lcm?!
def lcm(array):
    lcm = array[0]
    for i in range(1, len(array)):
        lcm *= array[i]//math.gcd(lcm, array[i])
    return lcm

timestamp = 0
buses = list()
bmax = 0
bpos = 0
with open(sys.argv[1]) as f:
    lines = f.readlines()
    timestamp = int(lines[0].strip())
    for i, bus in enumerate(lines[1].strip().split(',')):
        if bus != 'x':
            b = int(bus)
            # the most infrequent bus
            if b > bmax:
                bmax = b
                bpos = i
            buses.append([b, i])

print(timestamp)
print(buses)

t = 0
n = len(buses)
d = bmax
steps = 1
while True:
    # increment by the most infrequent bus
    t = (d * steps) - bpos
    print(t)
    t0 = t
    found = False
    matches = 0
    for i in range(n):
        bus = buses[i]
        t = t0 + bus[1]
        print(t, bus)
        q, r = divmod(t, bus[0])
        if r == 0:
            matches += 1
            if matches == n:
                print(t0)
                found = True
                break
        else:
            break

    if found:
        break
    else:
        steps += 1 

