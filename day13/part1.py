
import sys

timestamp = 0
buses = list()
with open(sys.argv[1]) as f:
    lines = f.readlines()
    timestamp = int(lines[0].strip())
    for bus in lines[1].strip().split(','):
        if bus != 'x':
            buses.append(int(bus))

buses.sort()
print(timestamp)
print(buses)

t = timestamp
bus = None
while True:
    print(t)
    for b in buses:
        q, r = divmod(t, b)
        if r == 0:
            bus = b
            break
    if bus is not None:
        print(t, bus)
        break
    else:
        t += 1

print(bus * (t - timestamp))
