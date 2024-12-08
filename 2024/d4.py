import sys; from pathlib import Path; sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))
from aoc import *

iday = 4
iyear = 2024

test1 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
test2 = None
test_ans_1 = 18
test_ans_2 = 9
sub = True
b = True
test_f = True

def run(data):
    p1 = 0
    p2 = 0

    grid = dict_grid(data)
    for p in grid.keys():
        if (grid[p] != "X"):
            continue
        st = "MAS"
        for o in offsets:
            s = ""
            for i in range(1, 4):
                s += (grid[p + i*o])
            if (s == st):
                p1 += 1

    for p in grid.keys():
        if (grid[p] != "A"):
            continue
        t = ("S", "M")
        if (grid[p+(1,1)] != grid[p-(1,1)] and grid[p+(1,-1)] != grid[p-(1,-1)]):
            a = True
            for i in (-1, 1):
                for j in (-1, 1):
                    if (grid[p+(i,j)] not in t):
                        a = False

            if a:
                p2 += 1
    
    return p1, p2

do_run(run, test1, test2, test_ans_1, test_ans_2, sub, iday, iyear, b, test_f)

