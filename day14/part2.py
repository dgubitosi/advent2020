
import sys

memory = dict()
with open(sys.argv[1]) as f:
    mask = None
    for line in f:
        a, b = line.strip().split(' = ')
        print(a,b)
        if a == 'mask':
            mask = b
        else:
            location = int(a.split('[')[-1][0:-1])
            value = int(b)

            # mask now affects the memory location
            location = [ c for c in "{:036b}".format(location) ]
            for index, bit in enumerate(mask):
                if bit in [ '1', 'X' ]: location[index] = bit

            # calculate all possible memory locations given the mask
            x_count = location.count('X')
            for i in range(2**x_count):
                bits = [ c for c in "{:036b}".format(i)[::-1] ]
                resolved_location = list()
                resolved_location.extend(location)
                # substiute the floating bits in MSB order
                for index in reversed(range(x_count)):
                    x_index = resolved_location.index('X')
                    resolved_location[x_index] = bits[index]
                address = int("".join(resolved_location), 2)
                print(i, address)
                memory.setdefault(address, 0)
                memory[address] = value

total = 0
for location in sorted(memory):
    integer = memory[location]
    print(location, integer)
    total += integer
print(total)
