import fileinput




level = 0 

n = 0
for line in fileinput.input():
    print(line)
    if level == 0:
        n = int(line)
    else:

    level += 1