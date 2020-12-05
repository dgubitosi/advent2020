
import sys

rows = 128
cols = 8
empty = '.'
occupied = 'X'
seats = [[ empty for x in range(cols)] for y in range(rows)]

max = 0
with open(sys.argv[1]) as f:
    for line in f:
        bp = line.strip()
        y = [0, rows-1]
        x = [0, cols-1]
        for i in range(len(bp)):
            c = bp[i]
            if c in 'FB':
                dy = (y[1] - y[0]) >> 1
                if c == 'F': y[1] = y[1] - dy - 1
                if c == 'B': y[0] = y[0] + dy + 1
            if c in 'LR':
                dx = (x[1] - x[0]) >> 1
                if c == 'L': x[1] = x[1] - dx - 1
                if c == 'R': x[0] = x[0] + dx + 1
            #print(c, tuple(y), tuple(x))
        r = y[0]
        c = x[0]
        seat = r * cols + c
        if seat > max: max = seat
        #print(bp, tuple([r, c]), seat)
        seats[r][c] = occupied

for r in range(len(seats)):
    s = ''.join(seats[r])
    #print(s)
    if occupied + empty + occupied in s:
        c = s.find(empty)
        print(r * cols + c)
        break
