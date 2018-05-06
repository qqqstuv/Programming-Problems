



import fileinput

testCase = 0






divider = 0
total = 0
count = 0
for line in fileinput.input():
	if testCase == 0:
		testCase = int(line.strip())
	elif line.strip() == "":
		pass
	else:
		if divider == 0:
			divider = int(line.strip())
		else:
			count += 1
			candy = int(line.strip())
			total = (total + candy) % divider
			if count == divider:
				if total == 0:
					print ("YES")
				else:
					print("NO")
				count = 0
				total = 0
				divider = 0
