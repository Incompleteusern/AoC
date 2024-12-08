import re

def ints(s):
    return [int(x) for x in re.findall(r"\d+", s)]
    
ls = []

def comp_num(r, s):
    if (r == 0 and len(s) == 0):
        return 1
    if (r < 0 or len(s) == 0):
        return 0
    
    a = 0
    l = s.pop()
    if (r % l == 0):
        a += comp_num(r//l, s)
    if (r != l and str(r).endswith(str(l))):
        a += comp_num(int(str(r)[:-len(str(l))]), s)
    
    a += comp_num(r-l, s)
    
    s.append(l)
    return a

with open("input.txt", "r") as f:
    for l in f:
        t = ints(l)
        ls.append((t[0], t[1:]))

ans = 0
for l in ls:
    if (comp_num(l[0], l[1]) > 0):
        ans += l[0]
    
print(ans)