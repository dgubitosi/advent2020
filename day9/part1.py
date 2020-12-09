
import sys

try:
    preamble = int(sys.argv[2])
except:
    preamble = 25

def check(n):
    end = len(numbers)
    start = end - preamble
    for i in range(start, end):
        for j in range(i, end):
            if numbers[i] + numbers[j] == n: return True
    return False

numbers = []
i = -1
with open(sys.argv[1]) as f:
    for line in f:
        i += 1
        n = int(line.strip())
        if i < preamble:
            numbers.append(n)
        elif check(n):
            numbers.append(n)
        else:
            print(n)
            break

