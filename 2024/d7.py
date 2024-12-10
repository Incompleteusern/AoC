import sys; from pathlib import Path; sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))
from aoc import *

iday = 7
iyear = 2024

test1 = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
test2 = None
test_ans_1 = 3749
test_ans_2 = 11387
sub = True
test_f = True

def dpcombine(r, s, c):
    if (r == 0 and len(s) == 0):
        return True
    if (r < 0 or len(s) == 0):
        return False
    
    l = s.pop()
    if (dpcombine(r-l, s, c)):
            s.append(l)
            return True
    
    if (r % l == 0 and dpcombine(r//l, s, c)):
        s.append(l)
        return True
    
    if (c and r != l and str(r).endswith(str(l)) and dpcombine(int(str(r)[:-len(str(l))]), s, c)):
        s.append(l)
        return True

    s.append(l)
    return False

def run(data):
    p1 = 0
    p2 = 0

    ls = []
            
    for l in data:
        t = ints(l)
        ls.append((t[0], t[1:]))

    for l in ls:
        if (dpcombine(l[0], l[1], False) > 0):
            p1 += l[0]
        if (dpcombine(l[0], l[1], True) > 0):
            p2 += l[0]
    return p1, p2
do_run(run, test1, test2, test_ans_1, test_ans_2, sub, iday, iyear, test_f)

