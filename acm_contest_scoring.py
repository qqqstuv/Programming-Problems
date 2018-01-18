import fileinput




problems = dict()

totalTime = 0
totalSolve = 0
for line in fileinput.input():
	line = line.strip().split(" ")
	if len(line) != 1:
		time = int(line[0])
		problem = line[1]
		answer = line[2]
		if answer == 'right':
			if problem in problems:
				time += problems[problem]
			totalTime += time
			totalSolve += 1
		else:
			if problem not in problems:
				problems[problem] = 0
			problems[problem] += 20

print (totalSolve, totalTime)
