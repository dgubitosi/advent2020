
import sys

def printMatrix():
    occupied = 0
    for row in matrix:
        occupied += row.count('#')
        print(''.join(row))
    print('OCCUPIED:', occupied)

def is_occupied(n, m):
    if matrix[n][m] == '#': return True
    return False

def is_floor(n,m):
    if matrix[n][m] == '.': return True
    return False

def is_seat(n,m):
    return not is_floor(n,m)

# build matrix, n rows of m seats
matrix = list()
rows = 0
with open(sys.argv[1]) as f:
    for line in f:
        rows += 1
        matrix.append([ c for c in line.strip() ])
cols = len(matrix[0])

steps = 0
while True:
    print('STEPS:', steps)
    printMatrix()
    print()
    temp = [[ '.' for c in range(cols)] for r in range(rows)]
    changes = 0
    for r in range(rows):
        for c in range(cols):
            # skip floor
            if is_floor(r,c): continue
            occupied = 0

            # find the first seat in each direction
            # 0 = north
            # 7 0 1
            # 6 x 2
            # 5 4 3
            for d in range(8):
                # origin
                n = r
                m = c
                
                # deltas
                delta_n = 0 # change in row
                delta_m = 0 # change in col

                # N* row changes by -1
                if d in [7, 0, 1]: delta_n = -1
                # S* row changes by +1
                if d in [5, 4, 3]: delta_n = +1
                # E* col changes by +1
                if d in [1, 2, 3]: delta_m = +1
                # W* col changes by -1
                if d in [7, 6, 5]: delta_m = -1

                # keep following the direction until
                # we hit the edge or encounter a seat
                while True:
                    n += delta_n
                    m += delta_m
                    # hit the edge
                    if n < 0 or n >= rows or m < 0 or m >= cols:
                        break
                    # encountered a seat
                    if is_seat(n,m):
                        if is_occupied(n,m): occupied += 1
                        break

            temp[r][c] = matrix[r][c]
            # seat is not occupied
            if not is_occupied(r,c):
                # state changes when no visible seats are occupied
                if occupied == 0:
                    temp[r][c] = '#'
                    changes += 1
            # seat is occupied 
            else:
                # state changes when 5 or more visible seats are occupied
                if occupied >= 5:
                    temp[r][c] = 'L'
                    changes += 1
    matrix = temp
    steps += 1
    if changes == 0: break

