
import sys
import math

class Ferry(object):

    def __init__(self):
        # ferry starts at (0, 0)
        self.x = 0
        self.y = 0
        # waypoint starts at (+10, +1)
        self.wx = 10
        self.wy = 1

    def __str__(self):
        x = self.x
        xstr = 'East'
        if x < 0:
            x *= -1 
            xstr = 'West'

        y = self.y
        ystr = 'North'
        if y < 0:
            y *= -1
            ystr = 'South'

        wx = self.wx
        wxstr = 'East'
        if wx < 0:
            wx *= -1 
            wxstr = 'West'

        wy = self.wy
        wystr = 'North'
        if wy < 0:
            wy *= -1
            wystr = 'South'

        return "Position ({} {}, {} {}) -> Waypoint ({} {}, {} {})".format(
            xstr, x, ystr, y, wxstr, wx, wystr, wy)

    def command(self, string):
        string = string.strip()
        instruction = string[0]
        value = int(string[1:])
        print('**', str(self))
        if instruction in ['N','S','E','W']: 
            self.move(instruction, value)
        if instruction in ['L','R']: 
            self.turn(instruction, value)
        if instruction in ['F']: 
            self.forward(instruction, value)
        print('**', str(self))

    def move(self, instruction, value):
        print('MOVE', instruction, value)
        if instruction == 'N':
            self.wy += value
        if instruction == 'S':
            self.wy -= value
        if instruction == 'E':
            self.wx += value
        if instruction == 'W':
            self.wx -= value

    def turn(self, instruction, value):
        print('TURN', instruction, value)
        # left is positive, right is negative
        if instruction == 'R':
            value *= -1
        
        # waypoint position
        wx = self.wx + self.x
        wy = self.wy + self.y

        # angle to waypoint
        a = math.atan2(wy-self.y, wx-self.x)
        a = math.degrees(a)
        angle = a + value
        if angle < 0:
            angle += 360
        
        # distance to the way point
        distance = math.sqrt(((wx-self.x)**2) + ((wy-self.y)**2))

        # new waypoint position
        self.wx = int(distance * math.cos(math.radians(angle)))
        self.wy = int(distance * math.sin(math.radians(angle)))

    def forward(self, instruction, value):
        print('FORWARD', instruction, value)
        if instruction == 'F':
            self.x += self.wx * value
            self.y += self.wy * value

    def manhattan(self):
        return abs(self.x) + abs(self.y)

ferry = Ferry()
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        print(line)
        ferry.command(line.strip())
        print()

print(ferry.manhattan())