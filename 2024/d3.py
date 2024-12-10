import sys; from pathlib import Path; sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))
from aoc import *

iday = 3
iyear = 2024

test1 = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
test2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
test_ans_1 = 161
test_ans_2 = 48
sub = True
test_f = True

def run(data):
    p1 = 0
    p2 = 0
            
    d = True
    for l in data:
        for i in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", l):
            if (i[2] != ""):
                d = True
            elif (i[3] != ""):
                d = False
            else:
                if d:
                    p2 += int(i[0])*int(i[1])
                p1 += int(i[0])*int(i[1])

    return p1, p2

do_run(run, test1, test2, test_ans_1, test_ans_2, sub, iday, iyear, test_f)

