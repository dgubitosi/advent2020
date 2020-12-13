
import sys
import math

class Ferry(object):

    def __init__(self):
        # start at 0,0 facing east
        self.x = 0
        self.y = 0
        self.direction = 0 # east

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

        return "Position ({} {}, {} {}), Heading {}".format(
            xstr, x, ystr, y, self.direction)

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
            self.y += value
        if instruction == 'S':
            self.y -= value
        if instruction == 'E':
            self.x += value
        if instruction == 'W':
            self.x -= value

    def turn(self, instruction, value):
        print('TURN', instruction, value)
        # left is positive, right is negative
        if instruction == 'R':
            value *= -1
        print('ANGLE', value)
        self.direction += value
        if self.direction < 0:
            self.direction += 360

    def forward(self, instruction, value):
        print('FORWARD', instruction, value)
        if instruction == 'F':
            radians = self.direction * math.pi / 180
            distance = float(value)
            self.x += int(distance * math.cos(radians))
            self.y += int(distance * math.sin(radians))

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