import sys

valid = 0
with open(sys.argv[1]) as f:
    for line in f:
        cx, lx, password = line.strip().split(" ")
        check = [ int(x) for x in cx.split("-") ]
        letter = lx.replace(":", "")
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
