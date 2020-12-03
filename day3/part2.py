import sys
from dataclasses import dataclass

map = []
with open(sys.argv[1]) as f:
    for line in f:
        map.append(line.strip())

@dataclass
class Point:
    x: int
    y: int

product = 1
slopes = [ Point(1,1), Point(3,1), Point(5,1), Point(7,1), Point(1,2) ]
for s in slopes:
    trees = []
    pos = Point(0,0)
    while pos.y < len(map):
        w = len(map[pos.y])
        x = pos.x % w
        loc = map[pos.y][x]
        #print(pos, loc)
        if loc == "#":
            trees.append(Point(pos.x, pos.y))
        pos.x += s.x
        pos.y += s.y
    #print(trees)
    print(s, len(trees))
    product *= len(trees)
print(product)
