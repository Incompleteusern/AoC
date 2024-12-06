import re

def ints(s):
    return [int(x) for x in re.findall(r"\d+", s)]
    
grid = []
gi = 0
gj = 0

with open("input.txt", "r") as f:
    for l in f:
        if ("." in l):
            grid.append(list(l))
            if ("^" in l):
                gi = len(grid)-1
                gj = l.index("^")

print(f"{gi} {gj}")


m1 = -1
m2 = 0

ogi = gi
ogj = gj
P = 130

ose = []
ose.append((gi,gj,m1,m2))
while True:
    if (gi+m1 < 0 or gi+m1 > len(grid)-1 or gj+m2 < 0 or gj+m2 > len(grid[0])-1):
        break
    if (grid[gi+m1][gj+m2] == "#"):
        m1, m2 = m2, -m1
    else:
        gi += m1
        gj += m2

    ose.append((gi,gj,m1,m2))

print(ose)
print(len(set([(t[0],t[1]) for t in ose])))

