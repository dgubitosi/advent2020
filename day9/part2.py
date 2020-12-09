
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

def crack(n):
    end = len(numbers)
    for i in range(end-1):
        s = numbers[i]
        for j in range(i+1, end):
            s += numbers[j]
            if s < n: continue
            if s == n: return numbers[i:j+1]
            if s > n: break
    return []

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
            x = crack(n)
            if x:
                x.sort()
                print(n, x, x[0]+x[-1])
                break
