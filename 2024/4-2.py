import re

def ints(s):
    return [int(x) for x in re.findall(r"\d+", s)]
    
k = []
s = 0
with open("input.txt", "r") as f:
    for l in f:
        k.append(list(l.strip()))
n = len(k[0])

for a in range(len(k)-2):
    for i in range(n-2):
        if (k[a+1][i+1] == "A" and k[a][i] != k[a+2][i+2] and k[a][i+2] != k[a+2][i] and 
        k[a][i] in ("S", "M") and k[a][i+2] in ("S", "M") and k[a+2][i] in ("S", "M") and k[a+2][i+2] in ("S", "M")):
            s += 1

print(s)
