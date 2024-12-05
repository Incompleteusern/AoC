import re

def ints(s):
    return [int(x) for x in re.findall(r"\d+", s)]
    
    
rules = []
man = []
k = []
s = 0
with open("input.txt", "r") as f:
    for l in f:
        if ("|" in l):
            a,b = l.split("|")
            rules.append((int(a),int(b)))
        elif ("," in l):
            man.append(ints(l))

ans = 0
for m in man:
    s = True
    for rule in rules:
        try:
            a = m.index(rule[0])
            b = m.index(rule[1])
            if (a > b):
                s = False
        except ValueError:
            pass
    if (s):
        ans += m[(len(m)-1)//2]
        
print(ans)