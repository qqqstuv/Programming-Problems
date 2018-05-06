import fileinput
# https://open.kattis.com/problems/evilstraw

def evilStraw(string):
	HashDict = dict()
	for i in range(len(string)):
		if not HashDict.get(string[i]):
			HashDict[string[i]] = [i]
		else:
			HashDict[string[i]] += [i]
	# print (HashDict)
	hasOddInstance = False
	pivot = 0
	for key,value in HashDict.items():
		if len(value) % 2 == 1: # odd number of values
			if not hasOddInstance:
				hasOddInstance = True
				pivot = i
			else:
				print ("Impossible")
				return
	if len(string) % 2 == 1:
		midIndex = min(HashDict[pivot])
		

skip = True
import sys

for line in sys.stdin:
	if not skip:
		evilStraw(line.strip())
	else:
		skip = False