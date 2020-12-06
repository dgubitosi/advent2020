
import sys

groups = []
sum = 0
with open(sys.argv[1]) as f:
    g = list()
    for line in f:
        a = set(list(line.strip()))
        if not a:
            group = set.intersection(*g)
            sum += len(group)
            groups.append(group)
            g = list()
        else:
           g.append(a)
    group = set.intersection(*g)
    sum += len(group)
    groups.append(group)

print(groups)
print(sum)
