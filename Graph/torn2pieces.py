
import fileinput

firstLine = True

adjacentHashMap = dict()
count = 0
maxCount = 0
start =""
stop = ""
for line in fileinput.input():
	if firstLine:
		firstLine = False
		maxCount = int(line.strip())
	else:
		if count < maxCount:
			line = line.strip().split(" ")
			if not line[0] in adjacentHashMap:
				adjacentHashMap[line[0]] = set()

			for i in range(1, len(line)):
				adjacentHashMap[line[0]].add(line[i])
				if line[i] not in adjacentHashMap:
					adjacentHashMap[line[i]] = set()
				adjacentHashMap[line[i]].add(line[0])
		else:
			line = line.strip().split(" ")
			start = line[0]
			stop = line[1]
		count += 1



# print(adjacentHashMap)

visited = set()

queue = []
queue.append(([start], start))

path =[]
while len(queue) != 0:
	path,children = queue.pop()
	visited.add(children)
	if children == stop:
		path += [children]
		path.pop(0)
		answer = " ".join(path)
		print(answer)
		exit(0)
	for element in adjacentHashMap[children]:
		if element not in visited:
			queue.append((path + [children],element))
print("no route found")


