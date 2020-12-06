
import sys

groups = []
sum = 0
with open(sys.argv[1]) as f:
    g = set()
    for line in f:
        a = set(list(line.strip()))
        if not a:
            sum += len(g)
            groups.append(g)
            g = set()
        else:
            g |= a

    # last group if no blank line at the end
    sum += len(g)
    groups.append(g)

print(groups)
print(sum)
