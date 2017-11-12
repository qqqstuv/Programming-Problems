

string = "ABCD"

dictionary = []

def permutation(currentDict, currentString):
	if len(currentDict) == 0:
		dictionary.append(currentString)
	for char in currentDict:
		temp = currentString
		temp += char
		currentDict.remove(char)
		permutation(currentDict, temp)
		currentDict.append(char)

permutation(list(string), "")

print(dictionary)

