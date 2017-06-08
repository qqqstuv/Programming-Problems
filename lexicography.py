#Source: https://open.kattis.com/problems/lexicography
import math, sys
# Get number of permutations for a dictionary
def getPermutationNumber(d):
    if len(d) > 0:
        count = math.factorial(sum(d.values()))
        for i in list(d.values()):
            count = count // math.factorial(i)
        return count
    return 0

# given the current index of k and the frequency dictionary (sorted), return the index closer to k and the next character in the string
def operate(currentIndex, frequencyDict):
    if len(list(frequencyDict)) == 1:
        return [currentIndex, list(frequencyDict.keys())[0], frequencyDict]
    modifiedDict = frequencyDict.copy()
    # print(sorted(list(frequencyDict)))
    previous = currentIndex # reset it to be the currentIndex because we keep updating indexes
    for character in sorted(list(frequencyDict)): # sorted from highest order to lowest
        # print(character, modifiedDict)
        if modifiedDict.get(character) == 1:
            del modifiedDict[character]
        else:
            modifiedDict[character] -= 1
        # print("After remove", modifiedDict, getPermutationNumber(modifiedDict))
        currentIndex += getPermutationNumber(modifiedDict)
        # print("NextChar", character ,"lowerIndex", previous, "UpperIndex", currentIndex)
        if k  <= currentIndex: # found the upperbound, return the new currentIndex and the next char
            return [previous, character, modifiedDict]
        else: # readd that character to dict
            if modifiedDict.get(character):
                modifiedDict[character] += 1
            else:
                modifiedDict[character]  = 1
            previous = currentIndex # reset it to be the currentIndex because we keep updating indexes

for line in sys.stdin:
    input = line.split()
    k = int(input[1])
    string = input[0]
    if string == '#' and k == 0:
        break
    sortedString = ''.join(sorted(string))
    d = {x:sortedString.count(x) for x in sortedString}
    start = 0
    final = ""
    length = 0
    while start <= k and length < len(string):
       result = operate(start, d)
       start = result[0]
       final += result[1]
       d = result[2]
       length += 1
    print(final)
