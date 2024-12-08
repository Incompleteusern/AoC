import re

def ints(s):
    return [int(x) for x in re.findall(r"\d+", s)]
    
s = 0
with open("input.txt", "r") as f:
    d = True
    for l in f:
        for i in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", l):
            if (i[2] != ""):
                d = True
            elif (i[3] != ""):
                d = False
            elif d:
                s += int(i[0])*int(i[1])

print(s)