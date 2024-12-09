import sys; from pathlib import Path; sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))
from aoc import *

iday = 8
iyear = 2024

test1 = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
test2 = None
test_ans_1 = 14
test_ans_2 = 34
sub = True
b = True
test_f = True

def run(data):
    p1 = 0
    p2 = 0
    
    grid = dict_grid(data)

    s1 = set()
    s2 = set()
    a = 0
    l = list(grid.keys())
    M = len(grid[0]) + len(grid)
    for i in range(len(l)):
        if (grid[l[i]] == "."):
            continue
        for j in range(i+1, len(l)):
            if (i == j):
                continue

            if (grid[l[i]] == grid[l[j]]):

                for k in range(-M, M):
                    si = (k+1)*l[i]-(k*l[j])
                    if (si in grid.keys()):
                        s2.add(si)
                        if (k == 1 or k == -2):
                            s1.add(si)
    p1, p2 = len(s1), len(s2)

    return p1, p2
do_run(run, test1, test2, test_ans_1, test_ans_2, sub, iday, iyear, b, test_f)

