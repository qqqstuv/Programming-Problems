# https://open.kattis.com/problems/babylonian
import fileinput

def Babylonian(numList):
    base = 0
    exponent = len(numList) - 1
    for i in numList:
        if i != '':
            i = int(i)
            base += i * pow(60,exponent)
        exponent -= 1

    print(base)





skip = True
for line in fileinput.input():
    if not skip:
        Babylonian(line.strip().split(","))
    else:
        skip = False
