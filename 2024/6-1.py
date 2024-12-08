import sys; from pathlib import Path; sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))
from aoc import *

iday = 6
iyear = 2024

test1 = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
test2 = None
test_ans_1 = 41
test_ans_2 = 6
sub = False
b = True
test_f = True

P = 130

a = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def run_guard(g, walls, R, C, just_walls=False):
    t = 0
    #m1 = -1
    #m2 = 0
    seen = []
    loop = False
    p = 0
    while True:
        t = g + a[p]
        turn = False
        if (t in walls):
            # turn
            p = (p + 1) % 4
            #m1, m2 = m2, -m1
            turn = True
        elif (t.x < 0 or t.x >= R or t.y < 0 or t.y >= C):
            break
        else:
            g = t
        if not just_walls or turn:
            tu = (g,p)
            if tu in seen:
                
                loop = True
                break
            seen.append(tu)

    return seen, loop

def run(data):
    p1 = 0
    p2 = 0
    
    R = len(data)
    C = len(data[0])

    print(R)
    print(C)
    g = None

    walls = set()
    data = [x for x in data if x.strip() != ""]
    for r, l in enumerate(data):
        l = l.strip()
        for c, p in enumerate(l):
            k = P2(r,c)
            if p == "^":
                g = k
            elif p == "#":
                walls.add(k)

    seen, _ = run_guard(g, walls, R, C)
    p1 = len(set([t[0] for t in seen]))
    works = set()
    import time
    s = time.time()
    for ng, p in seen:
        f = ng+a[p]
        if (f in walls or f == g or f in works):
            continue

        walls.add(f)

        _, loop = run_guard(g, walls, R, C, True)
        if loop:
            works.add(f)
        
        walls.remove(f)
    print(time.time() - s)

    p2 = len(works)

    return p1, p2

do_run(run, test1, test2, test_ans_1, test_ans_2, sub, iday, iyear, b, test_f)

