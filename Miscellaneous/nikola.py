

import fileinput
import sys

firstLine = True

n = 0

cost = []

table = dict()	

def dp(currentPos, precededMove):
	key = str(currentPos) + "-" + str(precededMove)
	if key in table:
		return table[key]
	if currentPos == n - 1:
		return cost[currentPos]

	goForward = sys.maxsize
	if currentPos + precededMove + 1 < n:
		goForward = 0
		newMove = precededMove + 1
		goForward += cost[currentPos]
		goForward += dp(currentPos + newMove, newMove)

	goBack = sys.maxsize
	if currentPos - precededMove >= 0:
		goBack = 0
		goBack += cost[currentPos]
		goBack += dp(currentPos - precededMove, precededMove)



	answer = min(goBack, goForward)
	table[key] = answer
	return answer


def solve():
	result = dp(1,1)
	print(result)

for line in fileinput.input():
	if firstLine:
		firstLine = False
		n = int(line.strip())
	else:
		cost.append(int(line.strip()))

solve()
