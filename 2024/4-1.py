import re

def ints(s):
    return [int(x) for x in re.findall(r"\d+", s)]
    
k = []
s = 0
with open("input.txt", "r") as f:
    for l in f:
        k.append(list(l.strip()))
        s += l.count("XMAS")
        s += l.count("SAMX")
n = len(k[0])

for a in range(len(k)-3):
    for i in range(n-3):
        t = k[a][i] + k[a+1][i+1] + k[a+2][i+2] + k[a+3][i+3]
        if (t in ("XMAS", "SAMX")):
            s += 1
        t = k[a][i+3] + k[a+1][i+2] + k[a+2][i+1] + k[a+3][i]
        if (t in ("XMAS", "SAMX")):
            s += 1

for a in range(len(k)-3):
    for i in range(n):
        t = k[a][i] + k[a+1][i] + k[a+2][i] + k[a+3][i]
        if (t in ("XMAS", "SAMX")):
            s += 1

print(s)
