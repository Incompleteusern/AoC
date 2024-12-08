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
            for ist in range(-100, 100):
                si = (a + ist*(a-c),b+ist*(b-d))
                if (si in grid.keys()):
                    s.add(si)
print(len(s))