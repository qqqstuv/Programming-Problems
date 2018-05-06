

import sys


first = True
inp = []
maxNum = 0

for line in sys.stdin:
    if not first:
        entry = line.split()
        maxNum = max(maxNum, int(entry[1]))
        inp.append(int(entry[1]))
    first = False

def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = set()
    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.add(i)
    return primes

primes = primes_sieve(maxNum)

hashHappy = dict()

def isHappy(num, updateList):
    intList = [int(j) for j in str(num)]
    res = 0
    for j in intList:
        res += j**2
    if res == 1:
        for update in updateList:
            hashHappy[update] = "YES"
        return "YES"
    if hashHappy.get(res) == "YES":
        for update in updateList:
            hashHappy[update] = "YES"
        return "YES"
    elif hashHappy.get(res) == "NO":
        for update in updateList:
            hashHappy[update] = "NO"
        return "NO"
    if res in updateList:
        for update in updateList:
            hashHappy[update] = "NO"
        return "NO"
    else:
        updateList.add(res)
    return isHappy(res, updateList)

# inp = [i for i in range(300)]
idx = 1
for i in inp:
    result = "NO"
    if i in primes:
        result = isHappy(i, set())
    print(idx, i, result)
    idx += 1








