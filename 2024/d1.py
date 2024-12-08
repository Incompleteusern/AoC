import sys; from pathlib import Path; sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))
from aoc import *

iday = 1
iyear = 2024

test1 = """3   4
4   3
2   5
1   3
3   9
3   3"""
test2 = None
test_ans_1 = 11
test_ans_2 = 31
sub = True
b = True
test_f = True

def run(data):
    p1 = 0
    p2 = 0
    a = []
    b = []

    for l in data:
        a1,b1 = ints(l)
        a.append(a1)
        b.append(b1)

    a.sort()
    b.sort()
    p1 = 0
    p2 = 0
    for i in range(len(a)):
        p1 += abs(a[i] - b[i])
        p2 += a[i] * b.count(a[i])
            
    return p1, p2

do_run(run, test1, test2, test_ans_1, test_ans_2, sub, iday, iyear, b, test_f)