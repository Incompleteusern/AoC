import sys; from pathlib import Path; sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))
from aoc import *

iday = 5
iyear = 2024

test1 = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
test2 = None
test_ans_1 = 143
test_ans_2 = 123
sub = True
test_f = True

def run(data):
    p1 = 0
    p2 = 0
            
    for l in data:
        pass

    rules = []
    man = []
    for l in data:
        if ("|" in l):
            rules.append(ints(l))
        elif ("," in l):
            man.append(ints(l))

    for m in man:
        s = True
        while True:
            t = True
            for rule in rules:
                if (rule[0] not in m or rule[1] not in m):
                    continue

                a = m.index(rule[0])
                b = m.index(rule[1])
                if (a > b):
                    s = False
                    t = False
                    m[a], m[b] = rule[1], rule[0]
            if (t):
                break
        if (s):
            p1 += m[(len(m)-1)//2]
        else:
            p2 += m[(len(m)-1)//2]

            
    return p1, p2
do_run(run, test1, test2, test_ans_1, test_ans_2, sub, iday, iyear, test_f)


    
