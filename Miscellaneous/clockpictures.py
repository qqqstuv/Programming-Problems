
import fileinput

total = 0
first = []
second = []


def solve(firstString, secondString):
	firstString.sort()
	secondString.sort()

	firstStringArea = []
	for idx in range(1, len(firstString)):
		firstStringArea.append(firstString[idx] - firstString[idx - 1])
	firstStringArea.append(360000 - firstString[len(firstString) - 1] + firstString[0])

	secondStringArea = []
	for idx in range(1, len(secondString)):
		secondStringArea.append(secondString[idx] - secondString[idx - 1])
	secondStringArea.append(360000 - secondString[len(secondString) - 1] + secondString[0])

	secondStringArea += secondStringArea
 
	firstStringArea = ','.join('^%d' % (x,) for x in firstStringArea)

	secondStringArea = ','.join('^%d' % (x,) for x in secondStringArea)

	result = secondStringArea.find(firstStringArea, 0)
	if result == -1:
		print("impossible")
	else:
		print("possible")

for line in fileinput.input():
	if total == 0:
		total = int(line.strip())
	elif first == []:
		first = [int(i) for i in line.strip().split(" ")]
	else:
		second = [int(i) for i in line.strip().split(" ")]
		solve(first, second)

