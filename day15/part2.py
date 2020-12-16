
puzzle = [11,18,0,20,1,7]

d = dict()
for i, p in enumerate(puzzle):
    d.setdefault(p, [])
    d[p] = i

turn = len(puzzle)
last = 16
while True:
    age = 0
    try:
        age = turn - d[last]
        d[last] = turn
    except:
        d.setdefault(last, turn)

    turn += 1
    #print(turn, last, age)
    if turn % 10000 == 0: print(turn)
    if turn == 30000000:
        print(last)
        break

    last = age
