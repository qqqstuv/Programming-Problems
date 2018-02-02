

import fileinput

testCase = 0
num = 0
count = 1
for line in fileinput.input():
	if testCase == 0:
		testCase = line.strip()
	else:
		if num  == 0:
			num = int(line.strip())
		else:
			listInt = [int(i) for i in line.strip().split(" ")]
			aSet = set()
			for num in listInt:
				if num not in aSet:
					aSet.add(num)
				else:
					aSet.remove(num)
			string = "Case #" + str(count)  + ":"
			print(string, str(list(aSet)[0]))
			count += 1
			num = 0

