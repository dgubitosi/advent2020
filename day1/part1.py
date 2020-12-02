
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
        if x + y == 2020:
            print(x,y,x+y,x*y)
            done = True
            break
    if done:
        break
