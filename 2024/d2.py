import sys; from pathlib import Path; sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))
from aoc import *

iday = 2
iyear = 2024

test1 = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
test2 = None
test_ans_1 = 2
test_ans_2 = 4
sub = True
test_f = True

def check(report):
    l = list(zip(report[:-1], report[1:]))
        
    a = all([(abs(x-y) >= 1) and (abs(x-y) <= 3) for x,y in l])
    inc = all([x>y for x,y in l])
    dec = all([x<y for x,y in l])
    return a and (inc or dec)


def run(data):
    p1 = 0
    p2 = 0
            
    for l in data:
        c = ints(l)
        if (check(c)):
            p1 += 1
            p2 += 1
        else:
            for j in range(len(c)):
                t = c[:j] + c[j+1:]

                if (check(t)):
                    p2 += 1
                    break

    return p1, p2

do_run(run, test1, test2, test_ans_1, test_ans_2, sub, iday, iyear, test_f)

