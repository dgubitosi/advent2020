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
        count = password.count(letter)
        if check[0] <= count <= check[1]:
            valid += 1
            print(letter,count,check,password)
print(valid)
