def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    dictS1 = dict()
    for char in s1:
        if not dictS1.get(char):
            dictS1[char] = 0
        dictS1[char] += 1
    temp = dictS1.copy()
    matchSoFar = 0
    totalChar = len(s1)
    first = 0
    last = 0
    while last < len(s2):
        print(first, last, temp, s2[last])
        if s2[last] not in temp:
            print("Not in temp")
            temp = dictS1.copy()
            matchSoFar = 0
            first = last
        elif temp[s2[last]] == 0:
            print("In temp but 0")
            while s2[last] != s2[first]:
                first += 1
                temp[s2[first]] += 1
                matchSoFar -= 1
            first += 1
        else:
            print("In temp")
            matchSoFar += 1
            if matchSoFar == totalChar:
                return True
            temp[s2[last]] -= 1
        last += 1
        if last - first > len(s1):
            first = last - first
        print("MatchSoFar", matchSoFar)
    return False

print("hello", "ooolleoooleh")
print(checkInclusion("hello", "ooolleoooleh"))