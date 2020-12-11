
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
            for n in [r-1, r, r+1]:
                for m in [c-1, c, c+1]:
                    if n == r and m == c: continue
                    if n < 0 or n >= rows or m < 0 or m >= cols: continue
                    #print(tuple([r,c]), tuple([n,m]), is_occupied(n,m))
                    if is_occupied(n,m): occupied += 1
            temp[r][c] = matrix[r][c]
            # seat is not occupied
            if not is_occupied(r,c):
                # state changes when no adjacent seats are occupied
                if occupied == 0:
                    temp[r][c] = '#'
                    changes += 1
            # seat is occupied 
            else:
                # state changes when 4 or more adjacent seats are occupied
                if occupied >= 4:
                    temp[r][c] = 'L'
                    changes += 1
    matrix = temp
    steps += 1
    if changes == 0: break

