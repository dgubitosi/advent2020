
import sys
#from bitstring import bitarray

mem = dict()
with open(sys.argv[1]) as f:
    mask = None
    for line in f:
        a, b = line.strip().split(' = ')
        print(a,b)
        if a == 'mask':
            mask = b
        else:
            m = int(a.split('[')[-1][0:-1])
            mem.setdefault(m, 0)
            mem[m] = [ c for c in "{:036b}".format(int(b)) ]
            for index, bit in enumerate(mask):
                if bit != 'X':
                    mem[m][index] = bit

total = 0
for m in sorted(mem):
    binary = "".join(mem[m])
    integer = int(binary, 2)
    print(m, binary, integer)
    total += integer
print(total)