import re

def ints(s):
    return [int(x) for x in re.findall(r"\d+", s)]

grid = dict()    

ans = 0

with open("input.txt", "r") as f:
    r = 0
    for l in f:
        r += 1
        l = l.strip()
        for c in range(len(l)):
            grid[(r,c)] = l[c]

print(grid)

s = set()
a = 0
for i in grid.keys():
    if (grid[i] == "."):
        continue
    for j in grid.keys():
        if (i == j):
            continue
        if (grid[i] == grid[j]):
            a,b = i
            c,d = j
            s1 = (2*c-a,2*d-b)
            s2 = (2*a-c,2*b-d)
            if (s1 in grid.keys()):
                s.add(s1)
            if (s2 in grid.keys()):
                s.add(s2)

print(len(s))