
import sys

numbers = []
with open(sys.argv[1]) as f:
    lines = f.readlines()
    numbers = [ int(x.strip()) for x in lines ]

done = False
for i, x in enumerate(numbers):
    for j, y in enumerate(numbers):
        if i == j:
            continue
        for k, z in enumerate(numbers):
            if k == i or k == j:
               continue 
            if done:
                break
            if x + y + z == 2020:
                print(x,y,z,x+y+z,x*y*z)
                done = True
                break
    if done:
        break
