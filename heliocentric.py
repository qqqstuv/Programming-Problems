

import fileinput

def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def lcm(a, b):
	# print("gcd of ", a,b, gcd(a,b))
	return a * b / gcd(a,b)


def brute_force(a, b):
	for n in range(1, 365):
		m = (687 * n - b + a)
		if m % 365 == 0:
			m = m / 365
			break
	# print("m", m)
	ans = 365 * m - a
	return int(ans)


count = 1

for line in fileinput.input():
	a, b = [int(i) for i in line.strip().split(" ")]
	string = "Case " + str(count) + ":"
	count += 1
	if a == 0 and b == 0:
		print(string,0)
	else:
		remainingA = 364 - a
		remainingB = 686 - b
		print(string,brute_force(a, b))
		# print(remainingA, remainingB)
		# print(lcm(remainingA, remainingB))
