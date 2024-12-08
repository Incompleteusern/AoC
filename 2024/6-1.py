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

def run_guard(gx, gy, walls, R, f, just_walls=False, last=False, wallseen=None):
    tx = -1
    ty = -1
    #m1 = -1
    #m2 = 0
    seen = []
    loop = False
    p = 0
    
    while (not loop):

        #print(g)

        # jump ahead -- each time jumping ahead, add the old value to tu
        if (wallseen != None):
            #print(tu)
            tu = (gx, gy,p)
            while (tu in wallseen.keys()):

                nextx, nexty, nextp, id = wallseen[tu]

                #print(f"Attempting jump from {tu} to {next}, dir is {id}")
                #print(f"FAKE REMINDER {f}")

                if (id == 0):
                    if (f.x == gx):
                        #print("SAME LINE")
                        if (rangecheck(gx, nextx, f.x)):
                            #print("FAILED JUMP")
                            break
                else:
                    if (f.y == gy):
                        #print("FAILED JUMP")
                        if (rangecheck(gy, nexty, f.y)):
                            break
                if (tu in seen):
                    loop = True
                    #print(f"LOOP BREAK: {tu}")
                    break
                
                seen.append(tu)

                tu = (nextx, nexty, nextp)
                gx = nextx
                gy = nexty
                p = nextp

                #print("SUCCESSFUL JUMP") 
            
        tx = gx + a[p][0]
        ty = gy + a[p][1]
        turn = False

        # each time changing directions, add old to seen
        if (P2(tx, ty) in walls):                    
            if just_walls:
                tu = (gx, gy, p)
                if tu in seen:
                    loop = True
                    #print(f"LOOP BREAK: {tu}")

                    break
                seen.append(tu)

            # turn
            p = (p + 1) % 4
            #m1, m2 = m2, -m1
            turn = True
        else:
            # each time going forward, add old to seen
            if not just_walls:
                tu = (gx, gy, p)
                if tu in seen:
                    #print(f"LOOP BREAK: {tu}")

                    loop = True
                    break
                seen.append(tu)

            if (tx < 0 or tx >= R or ty < 0 or ty >= R):
                break

            gx = tx
            gy = ty

    if (last and not loop):
        seen.append((gx, gy, p))

    return seen, loop

def run(data):
    p1 = 0
    p2 = 0
    
    R = len(data)
    C = len(data[0])
    assert R == C

    gx = 0
    gy = 0

    walls = set()
    data = [x for x in data if x.strip() != ""]
    for r, l in enumerate(data):
        l = l.strip()
        for c, p in enumerate(l):
            k = P2(r,c)
            if p == "^":
                gx = r
                gy = c
            elif p == "#":
                walls.add(k)

    seen, _ = run_guard(gx, gy, walls, R, None)
    print(seen)
    #1/0
    
    wallseen, _ = run_guard(gx, gy, walls, R, None, True, True)
    wallseen = [(gx, gy, 0), *wallseen]

    import time
    s = time.time()

    #print(wallseen)
    wallt = dict()
    for i in range(len(wallseen)-1):
        x1, y1, p1 = wallseen[i]
        x2, y2, p2 = wallseen[i+1]
        if (x1 == x2):
            wallt[wallseen[i]] = (*wallseen[i+1], 0)
        elif (y1 == y2):
            wallt[wallseen[i]] = (*wallseen[i+1], 1)

    #print(wallt)

    p1 = len(set([(x,y) for x,y,p in seen]))
    works = set()
    for i, (x, y, p) in enumerate(seen):
        #print("---------------")
        ng = P2(x,y)
        f = ng+a[p]
        #print(f"FAKE {f}, {i/len(seen)}")
        if (f in walls or f == P2(gx, gy) or f in works):
            continue
        elif (f.x < 0 or f.x >= R or f.y < 0 or f.y >= R):
            continue


        walls.add(f)
        _, loop = run_guard(gx, gy, walls, R, f, True, wallseen=wallt)
        if loop:
            works.add(f)
            #print("WORKS")
        walls.remove(f)


    print(time.time() - s)

    p2 = len(works)

    return p1, p2

do_run(run, test1, test2, test_ans_1, test_ans_2, sub, iday, iyear, b, test_f)

