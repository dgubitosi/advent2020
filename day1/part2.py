
import sys

numbers = []
with open(sys.argv[1]) as f:
    lines = f.readlines()
    numbers = [ int(x.strip()) for x in lines ]

done = False
for i in range(0, len(numbers)):
    x = numbers[i]
    if done: break
    for j in range(i+1, len(numbers)):
        y = numbers[j]
        if done: break
        for k in range(j+1, len(numbers)):
            z = numbers[k]
            if x + y + z == 2020:
                print(x,y,z,x+y+z,x*y*z)
                done = True
                break
