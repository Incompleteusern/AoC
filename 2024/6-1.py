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


def rangecheck(a, b, c):
    return (a <= c and c <= b) or (b <= c and c <= a)

def run_guard(g, walls, R, f, just_walls=False, last=False, wallseen=None):
    t = 0
    #m1 = -1
    #m2 = 0
    seen = []
    loop = False
    p = 0
    while (not loop):

        #print(g)

        tu = (g,p)
        if (wallseen != None):
            #print(tu)
            while (tu in wallseen.keys()):

                e = wallseen[tu]

                id = e[1]


                next = e[0]
                pos = next[0]
                #print(f"Attempting jump from {tu} to {next}, dir is {id}")
                #print(f"FAKE REMINDER {f}")

                if (id == 0):
                    if (f.x == g.x):
                        #print("SAME LINE")
                        if (rangecheck(g.x, pos.x, f.x)):
                            #print("FAILED JUMP")
                            break
                else:
                    if (f.y == g.y):
                        #print("FAILED JUMP")
                        if (rangecheck(g.y, pos.y, f.y)):
                            break
                if (tu in seen):
                    loop = True
                    #print(f"LOOP BREAK: {tu}")
                    break
                seen.append(tu)

                tu = next
                g = pos
                p = next[1]

                #print("SUCCESSFUL JUMP")

            
            
        t = g + a[p]
        turn = False

        if (t in walls):
            tu = (t,p)
                    
            if just_walls:
                tu = (g,p)
                if tu in seen:
                    loop = True
                    #print(f"LOOP BREAK: {tu}")

                    break
                seen.append(tu)

            # turn
            p = (p + 1) % 4
            #m1, m2 = m2, -m1
            turn = True
        elif (t.x < 0 or t.x >= R or t.y < 0 or t.y >= R):
            break
        else:
            g = t
        if not just_walls:
            tu = (g,p)
            if tu in seen:
                #print(f"LOOP BREAK: {tu}")

                loop = True
                break
            seen.append(tu)

    if (last and not loop):
        seen.append((g, p))

    return seen, loop

def run(data):
    p1 = 0
    p2 = 0
    
    R = len(data)
    C = len(data[0])
    assert R == C

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

    seen, _ = run_guard(g, walls, R, None)
    
    wallseen, _ = run_guard(g, walls, R, None, True, True)
    wallseen = [(g, 0), *[x for x in wallseen]]

    print(wallseen)
    wallt = dict()
    for i in range(len(wallseen)-1):
        a1 = wallseen[i][0]
        b1 = wallseen[i+1][0]
        if (a1.x == b1.x):
            wallt[wallseen[i]] = (wallseen[i+1], 0)
        elif (a1.y == b1.y):
            wallt[wallseen[i]] = (wallseen[i+1], 1)

    print(wallt)
    1/0

    p1 = len(set([t[0] for t in seen]))
    works = set()
    import time
    s = time.time()
    for i, (ng, p) in enumerate(seen):
        #print("---------------")

        f = ng+a[p]
        #print(f"FAKE {f}, {i/len(seen)}")
        if (f in walls or f == g or f in works):
            continue
        elif (f.x < 0 or f.x >= R or f.y < 0 or f.y >= R):
            continue


        walls.add(f)
        _, loop = run_guard(g, walls, R, f, True, wallseen=wallt)
        if loop:
            works.add(f)
            #print("WORKS")
        walls.remove(f)


    print(time.time() - s)

    p2 = len(works)

    return p1, p2

do_run(run, test1, test2, test_ans_1, test_ans_2, sub, iday, iyear, b, test_f)

