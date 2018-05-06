import fileinput


index = 0

timeLap = 0
numAtoB = 0
numBtoA = 0
for line in fileinput.input():
    print(line)
    if index == 1:
        timeLap = int(line)
    if index == 2:
        numAtoB = int(line.split()[0])
        numBtoA = int(line.split()[1])
    if index
    index += 1

