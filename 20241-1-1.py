
array1 = []
array2 = []

with open('input.txt', 'r') as f: #open the file
    contents = f.readlines() #put the lines to a variable (list).
    print(contents)
    for x in contents:
        t = x.split("   ")
        print(t)
        a = int(t[0])
        b = int(t[1].strip("\n"))
        array1.append(a)
        array2.append(b)

array1.sort()
array2.sort()

k = 0
for i in range(len(array1)):
    z = abs(array1[i] - array2[i])
    k += z
        
print(k)
