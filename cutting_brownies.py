




import fileinput, sys

firstLine = True
num = 0
B = 0
D = 0
isHorizontal = False

def cut(brownie, isHorizontal):
	newBrownies = []
	if isHorizontal:
		if brownie[1] <= 1:
			return newBrownies

		for i in range(1, brownie[1] // 2 + 1):
			newBrownies.append([ [brownie[0], i], [brownie[0],brownie[1]-i] ])
	else:
		if brownie[0] <= 1:
			return newBrownies

		for i in range(1, brownie[0] // 2 + 1):
			newBrownies.append([ [i, brownie[1]], [brownie[0]-i, brownie[1]] ])
	return newBrownies	



def solve():
	


for line in fileinput.input():
    if firstLine:
    	firstLine = False
    	num = int(line.strip())
    else:
    	line = [i for i in line.strip().split(" ")]
    	B = int(line[0])
    	D = int(line[1])
    	isHorizontal = False
    	if line[2] == 'Harry':
    		isHorizontal = True
    	solve()
