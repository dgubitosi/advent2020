
import sys

fields = [
  "byr", # Birth Year
  "iyr", # Issue Year
  "eyr", # Expiration Year
  "hgt", # Height
  "hcl", # Hair Color
  "ecl", # Eye Color
  "pid", # Passport ID
  "cid", # Country ID, optional
]

r = dict()
records = []
with open(sys.argv[1]) as f:
    for line in f:
        parts = line.strip().split()
        if not parts:
            if r: records.append(r)
            r = dict()
            continue
        for p in parts:
            k,v = p.split(':')
            if k in fields:
                r.setdefault(k, []).append(v)
    # dont forget the last record
    if r: records.append(r)

valid = 0
for r in records:
    k = r.keys()
    n = len(k)
    if (n == 8) or (n == 7 and 'cid' not in k):
        valid += 1
        print("V", k)
    else:
        print("*", k)
print(valid)

