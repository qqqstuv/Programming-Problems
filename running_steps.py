

import fileinput, math

firstLine = True


memo = dict()


def solve(num):
	half = num // 2
	ans = 0
	pairs = []
	for i in range(1, half + 1):
		for j in range(i + 1):
			if j + i * 2 == half:
				pairs.append([j,i])
	for pair in pairs:
		permutation = math.factorial(pair[0] + pair[1]) // (math.factorial(pair[0]) * math.factorial(pair[1]))
		ans += permutation * permutation
	return ans



firstLine = True

for line in fileinput.input():
	if firstLine:
		firstLine = False
	else:
		count, num = [int(i) for i in line.strip().split(" ")]
		ans = solve(num)
		print(count,ans)