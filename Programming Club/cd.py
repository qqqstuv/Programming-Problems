

import fileinput


N = 0
M = 0
Ndict = set()

count = 0
result = 0
for line in fileinput.input():
	line =  [int(i) for i in line.strip().split(" ")]
	if N == 0:
		N = line[0]
		M = line[1]
	elif len(line) == 2:
		print(result)
	else:
		if count < N:
			Ndict.add(line[0])
		else:
			if line[0] in Ndict:
				result += 1
		count += 1
