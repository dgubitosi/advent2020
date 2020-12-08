
import sys

with open(sys.argv[1]) as f:
    program = f.readlines()

acc = 0
pc  = 0
ppc = []

line = program[pc]
while line:
    if pc in ppc:
        print(acc)
        break
    instruction, value = line.strip().split(' ', 2)
    print(instruction, value)
    ppc.append(pc)
    if instruction == 'nop':
        pc += 1
    if instruction == 'acc':
        acc += int(value)
        pc += 1
    if instruction == 'jmp':
        pc += int(value)
    line = program[pc]
