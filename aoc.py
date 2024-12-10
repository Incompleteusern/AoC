from aocd import get_data, submit
import re
from collections import defaultdict

def ints(s):
    return [int(x) for x in re.findall(r"\d+", s)]
    
def run_test(run, data1, data2, ansA, ansB):
    if (data1 == None):
        print("Skipping Testing!")
        return
    result_a, result_b = run(data1)
    if (data2 != data1):
        _, result_b = run(data2)

    t = []

    te = [(result_a, ansA, "Part a"), ((result_b, ansB, "Part b"))]


    for (result, ans, name) in te:
        if (ans == None):
            print(f"Skipping {name} Test!")
            continue
    
        if (result == ans):
            print(f"{name} case passes.")
            t.append(True)
        else:
            print(f"{name} failed, got {result} instead of {ans}")
            t.append(False)

    return t

def do_run(run: int, test1: str | None, test2: str | None, test_ans_a: int | None, test_ans_b: int | None, sub: bool, iday: int, iyear: int, test_f=True):
    if (test2 == None):
        test2 = test1
    
    data = get_data(day=iday, year=iyear)
        
    t = run_test(run, test1.split("\n"), test2.split("\n"), test_ans_a, test_ans_b)
    if (test_f and not all(t)):
        return

    ansA, ansB = run(data.split("\n"))
    print(f"Part a Output: {ansA}")
    print(f"Part b Output: {ansB}")

    if (sub and t[0]):
        submit(ansA, part="a", day=iday, year=iyear)
    if (sub and t[1]):
        submit(ansB, part="b", day=iday, year=iyear)

#############

class QuietDict(dict):
    def __init__(self, default):
        self.default = ""

    def __missing__(self, key):
        return self.default


def dict_grid(data, default = ""):
    # nice idea from tenth
    data = [x for x in data if x.strip() != ""]
    grid = QuietDict("")
    for r, l in enumerate(data):
        l = l.strip()
        for c, p in enumerate(l):
            grid[P2(r,c)] = p
    return grid

class P2:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    #https://stackoverflow.com/questions/19458291/efficient-vector-point-class-in-python
    def __abs__(self):
        return P2(abs(self.x), abs(self.y))

    def __int__(self):
        return P2(int(self.x), int(self.y))

    def __add__(self, other):
        if isinstance(other, tuple) or isinstance(other, list):
            return P2(self.x + other[0], self.y + other[1])

        return P2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, tuple) or isinstance(other, list):
            return P2(self.x - other[0], self.y - other[1])

        return P2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return P2(self.x * other, self.y * other)

    def __div__(self, other):
        return P2(self.x / other, self.y / other)

    def __rmul__(self, other):
        return P2(self.x * other, self.y * other)

    def __rdiv__(self, other):
        return P2(self.x / other, self.y / other)
    
    def __eq__(self, other):
        if isinstance(other, P2):
            return self.x == other.x and self.y == other.y
        return False
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"

offsets = [
        P2(0,1), P2(1,0), P2(1,1), P2(-1,1),
        P2(0,-1), P2(-1,0), P2(-1,-1), P2(1,-1)
]

