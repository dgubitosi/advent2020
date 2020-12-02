import sys

valid = 0
with open(sys.argv[1]) as f:
    for line in f:
        cx, lx, password = line.strip().split(" ")
        check = [ int(x) for x in cx.split("-") ]
        letter = lx.replace(":", "")
        count = password.count(letter)
        if check[0] <= count <= check[1]:
            valid += 1
            print(letter,count,check,password)
print(valid)
