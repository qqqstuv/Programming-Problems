import fileinput

firstLine = True
total = 0
prohibitDict = dict()

def geppetto(testList):
	# print(testList)
	totalSum = 0
	if len(testList) != 0:
		test = testList[0]
		# print(test)
		testList.remove(test)
		# print("recursive no for", test, " with list ", testList)
		new_list = list(testList)
		notTakeSum = geppetto(new_list)
		# print("notTakeSum", notTakeSum)
		new_list = list(testList)
		for i in prohibitDict[test]:
			if i in new_list:
				new_list.remove(i)
		# print("recursive yes for ", test, " with list ", testList)
		takeSum = geppetto(new_list)
		totalSum += takeSum
		totalSum += notTakeSum
		# print("takeSum", takeSum)
		# print("totalSum", totalSum, test)
		return totalSum
	return 1
read = 0
hasRead = -1
for line in fileinput.input():
	if hasRead == read:
		break
	hasRead += 1
	if firstLine:
		firstLine = False
		total = int(line.split(" ")[0])
		read = int(line.split(" ")[1])
		for i in range(0, total + 1):
			prohibitDict[i] = []
	else:
		prohibit =[int(i) for i in line.split(" ")]

		prohibitDict[prohibit[0]].append(prohibit[1])
		prohibitDict[prohibit[1]].append(prohibit[0])

testList = [ i for i in range(1, total + 1)]

# print(prohibitDict)
result = geppetto(testList)
print(result)




