

import fileinput

firstLine = True

cities = 0
pilots = 0

for line in fileinput.input():
	if firstLine:
		firstLine = False
	else:
		if pilots == 0:
			cities, pilots = [int(i) for i in line.strip().split(" ")]
			print(cities - 1)
		else:
			pilots -= 1