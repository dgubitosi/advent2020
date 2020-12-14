
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
            memory.setdefault(location, 0)
            memory[location] = [ c for c in "{:036b}".format(int(b)) ]
            for index, bit in enumerate(mask):
                if bit != 'X':
                    memory[location][index] = bit

total = 0
for location in sorted(memory):
    binary = "".join(memory[location])
    integer = int(binary, 2)
    print(location, binary, integer)
    total += integer
print(total)
