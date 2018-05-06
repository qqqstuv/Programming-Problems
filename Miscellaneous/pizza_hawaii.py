

import fileinput



def solve(ingredients, guess):
	hashDict = dict()
	for i in range(len(ingredients)):
		for ingredient in ingredients[i]:
			if ingredient not in hashDict:
				hashDict[ingredient] = guess[i]
			else:
				for a_guess in guess:
					



testCase = 0
pizza_num = 0
name = 1
count = 0
ingredients = []
guess = []
pizza_count = 0


for line in fileinput.input():
	if testCase == 0:
		testCase = int(line.strip())
	elif pizza_num == 0:
		pizza_num = int(line.strip())
		# print("PIZZA NUM", pizza_num)

	else:
		if name == 1:
			name = line.strip()
			# print("setname", name)
		else:
			# print("line", line)
			if count == 0:
				ingredients.append(line.strip().split(" ")[1:])
			elif count == 1:
				guess.append(line.strip().split(" ")[1:])
				count = -1
				name = 1
				pizza_count += 1
				if pizza_count == pizza_num:
					solve(ingredients, guess)
					pizza_count = 0
					pizza_num = 0
					ingredients = []
					guess = []

			count += 1


