import re

def ints(s):
    return [int(x) for x in re.findall(r"\d+", s)]
    
s = 0
with open("input.txt", "r") as f:
    for l in f:
        s += sum([int(i[0][0])*int(i[1][1]) for i in zip(re.findall(r"mul\((\d+),(\d+)\)", l), re.findall(r"mul\((\d+),(\d+)\)", l))])

print(s)