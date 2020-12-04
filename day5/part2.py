
import re
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

def between(v, a, b):
    if a <= v <= b: return True
    return False

def byr(v, a=1920, b=2020):
    return between(int(v), a, b)

def iyr(v, a=2010, b=2020):
    return between(int(v), a, b)

def eyr(v, a=2020, b=2030):
    return between(int(v), a, b)

def hgt(v):
    if v.endswith('cm'):
        h = v.split('cm')[0]
        return between(int(h), 150, 193)
    if v.endswith('in'):
        h = v.split('in')[0]
        return between(int(h), 59, 76)
    return False

def hcl(v):
    if re.match(r'^#[0-9a-f]{6}$', str(v)): return True
    return False

def ecl(v):
    colors = [ "amb", "blu", "brn", "gry", "grn", "hzl", "oth" ]
    if v in colors: return True
    return False

def pid(v):
    if re.match(r'^[0-9]{9}$', str(v)): return True
    return False

def cid(v):
    return True

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
    is_valid = False
    if (n == 8) or (n == 7 and 'cid' not in k):
        is_valid = True
        for field in k:
            validate = globals()[field]
            if len(r[field]) != 1 or not validate(r[field][0]):
                is_valid = False
                break
    if is_valid:
        valid += 1
        print("V", r)
    else:
        print("*", r)
print(valid)

