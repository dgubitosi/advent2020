
import sys

with open(sys.argv[1]) as f:
    program = f.readlines()

tested = [ None ]

i = 0
loop = True
while loop:
    i +=1 
    print(i, tested)

    loop = False
    switched = False
    acc = 0
    pc  = 0
    ppc = []

    line = program[pc]
    while line:
        if pc in ppc:
            loop = True
            break

        instruction, value = line.strip().split(' ', 2)
        print(instruction, value)
        ppc.append(pc)

        switch = [ 'nop', 'jmp' ]
        if not switched and pc not in tested and instruction in switch:
            switched = True
            tested.append(pc)
            index = switch.index(instruction)
            instruction = switch[index-1]

        if instruction == 'nop':
            pc += 1
        if instruction == 'acc':
            acc += int(value)
            pc += 1
        if instruction == 'jmp':
            pc += int(value)
        
        try:
            line = program[pc]
        except:
            # terminate when pc is outside of program space
            print(tested)
            print(acc)
            loop = False
            break
