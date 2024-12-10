import sys; from pathlib import Path; sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))
from aoc import *

iday = 10
iyear = 2024

test1 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
test2 = None
test_ans_1 = 36
test_ans_2 = 81
sub = True
test_f = True

def run(data):
    p1 = 0
    p2 = 0

    grid = dict_grid(data)

    score = dict()
    score2 = dict()

    for i in range(9, -1, -1):
        for k in grid.keys():
            if (grid[k] != str(i)):
                continue
            if (i == 9):
                score[k] = set([k])
                score2[k] = 1
            else:
                s = set()
                s2 = 0
                for p in [P2(-1,0),P2(1,0),P2(0,1),P2(0,-1)]:
                    if (grid[k+p] == str(i+1)):
                        s = s.union(score[k+p])
                        s2 += score2[k+p]
                score[k] = s
                score2[k] = s2
                if (i == 0):
                    p1 += len(s)
                    p2 += s2

    return p1, p2
do_run(run, test1, test2, test_ans_1, test_ans_2, sub, iday, iyear, test_f)

