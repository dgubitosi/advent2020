import re
import sys

valid = 0
p = re.compile(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')
with open(sys.argv[1]) as f:
    for line in f:
        m = p.search(line)
        check = [ int(m.group(1)), int(m.group(2)) ]
        letter = m.group(3)
        password = m.group(4)
        try:
            x = password[check[0]-1] == letter
        except:
            x = False
        try:
            y = password[check[1]-1] == letter
        except:
            y = False
        if (x ^ y):
           valid += 1
           print(letter,check,x,y,password)
print(valid)
