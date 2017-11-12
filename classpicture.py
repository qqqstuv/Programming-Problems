

import fileinput

peopleNum = 0
pairNum = 0

people = []
pair = []
def solve():

for line in fileinput.input():
	if peopleNum == 0:
		peopleNum = int(line.strip())
	elif len(people) != peopleNum:
		people.append(line.strip())
	elif pairNum == 0:
		pairNum = int(line.strip())
	elif len(pair) != pairNum:

		solve()
