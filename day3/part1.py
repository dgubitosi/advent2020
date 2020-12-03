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

trees = []
pos = Point(0,0)
while pos.y < len(map):
    w = len(map[pos.y])
    x = pos.x % w
    loc = map[pos.y][x]
    print(pos, loc)
    if loc == "#":
        trees.append(Point(pos.x, pos.y))
    pos.x += 3
    pos.y += 1
print(trees)
print(len(trees))
