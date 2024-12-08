def check(report):
    a = True
    inc = True
    dec = True
    for i in range(len(report)-1):
        a = a and abs(report[i+1]-report[i]) >= 1
        a = a and abs(report[i+1]-report[i]) <= 3
        inc = inc and report[i+1] > report[i]
        dec = dec and report[i+1] < report[i]
    return a and (inc or dec)
k = 0
with open("input.txt", "r") as f:
    for lines in f:
        report = lines.split()
        print(report)
        print(check([int(x) for x in report]))
        if any([check([int(report[el]) for el in range(len(report)) if el != i]) for i in range(len(report))]):
            k += 1
print(k)