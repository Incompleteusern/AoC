import sys; from pathlib import Path; sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))
from aoc import *

iday = 9
iyear = 2024

test1 = """2333133121414131402"""
test2 = None
test_ans_1 = 1928
test_ans_2 = 2858
sub = False
test_f = True

offset = ord("0")

def compact1(l):
    s = ""
    t = 0
    
    ocount = []
    for i in [int(x) for x in l]:
        if (t % 2 == 0):
            s += (chr(t//2 + offset)*i)
            ocount.append(i)
        else:
            s += " "*i
        t += 1

    scount = s.count(" ")
    for i in range(t//2, -1, -1):
        o = chr(i + offset)
        oc = ocount[i]

        m = min(oc, scount)
        s = s.replace(" ", o, m)[:-m]
        scount -= m
        if (scount <= 0):
            break

    k = 0
    for c, i in enumerate(list(s)):
        if (ord(i) < offset):
            continue
        k += (ord(i)-offset)*c
    
    return k

def compact2(l):
    s = ""
    t = 0
    
    ocount = []
    oindex = []

    li = 0
    for i in [int(x) for x in l]:
        if (t % 2 == 0):
            s += (chr(t//2 + offset)*i)
            ocount.append(i)
            oindex.append(li)
        else:
            s += " "*i
        t += 1
        li += i


    i = t//2 + 1
    for i in range(t//2, -1, -1):
        o = chr(i + offset)
        oi = oindex[i]
        oc = ocount[i]
        t = s.find(" "*ocount[i], 0, oi)

        if (t == -1):
            continue
        
        s = s[:t] + o*oc + s[t+oc:].replace(o, " ")

    k = 0
    for c, i in enumerate(list(s)):
        if (ord(i) < offset):
            continue
        k += (ord(i)-offset)*c
    
    return k

def old(l):
    s = []
    t = 0
    
    for i in [int(x) for x in l]:
        if (t % 2 == 0):
            for k in range(i):
                s.append(t//2)
        else:
            for k in range(i):
                s.append(-1)
        t += 1

    while (-1 in s):
        c = s.pop()
        if (c != -1):
            s[s.index(-1)] = c     

    k = 0
    for c, i in enumerate(s):
        k += c*i

    return k

def old2(l):
    files = []
    spaces = []
    file = 0

    li = 0
    for i in [int(x) for x in l]:
        if (file % 2 == 0):
            files.append([file//2, li, i])
        else:
            spaces.append([li, i])
                
        file += 1
        li += i

    processed_files = []
    while (len(files) > 0):
        print(len(files))
        file = files.pop()
        n, index, size = file
        
        try_add = False
        for space_list_index, (s_index, s_size) in enumerate(spaces):

            if (s_size < size):
                continue
            if (s_index > index):
                break
            
            try_add = True
            processed_files.append([n, s_index, size])

            if (s_size == 0):
                del spaces[space_list_index]
            else:
                spaces[space_list_index] = [s_index+size, s_size - size]

            break

        if (not try_add):
            processed_files.append(file)

    print(processed_files)
            

    k =0
    for file in processed_files:
        n, index, size = file
        for i in range(index, index+size):
            k += i*n
        #print(f"{i} {c}")
    #print(k)
    return k

def run(data):
    p1 = 0
    p2 = 0
            
    for l in data:
        p1 = compact1(l)
        p2 = compact2(l)

    return p1, p2
do_run(run, test1, test2, test_ans_1, test_ans_2, sub, iday, iyear, test_f)

