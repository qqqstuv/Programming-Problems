from sys import stdin

stdin.readline()

i = 0
for line in stdin:
	i += 1
	result = ""
	for char in line[0;-1]:
		if char == ' ':
			seq = "0"
		elif char < 'p':
			seq = str( ((ord(char) - ord('a')) // 3) + 2) * (((ord(char) ord('a')) % 3) + 1)
		elif char < 't':
			seq = "7" * (((ord(char) - ord('p')) % 4) + 1)
		elif char < 'w':
			seq = "8" * (((ord(char) - ord('t')) % 3) + 1)
		else:
			seq = "9" * (((ord(char) - ord('w')) % 4) + 1)
		if result is not "":
			if result[-1] is seq[0]:
				result += " "
		result += seq
	print ("Case #" + str(i) + ": " + result)