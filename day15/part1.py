
puzzle = [11,18,0,20,1,7,16]
puzzle.reverse()

while True:
    number = puzzle[0]
    try:
        index = puzzle.index(number, 1)
        puzzle.insert(0, index)
    except:
        puzzle.insert(0, 0)

    if len(puzzle) == 2020:
        print(puzzle[0])
        break
print(puzzle)
