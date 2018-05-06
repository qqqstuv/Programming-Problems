import fileinput,sys


firstLine = True


class Solve(object):
    def fruitbasket(self, weights, isOne):
        self.absolute = 0
        lessWeights = []
        for x in weights:
        	if x < 200:
        		lessWeights.append(x)
        self.totalSubtractSum = 0
        if isOne:
        	self.subtractLessWeight(lessWeights, 0)
        else:
        	self.comb(lessWeights, -1, 0)
        lessThanSum = 0
        self.absolute -= self.totalSubtractSum
        multiply = 2**(len(weights) - 1)
        for weight in weights:
        	self.absolute += weight * multiply
        print(self.absolute)

    def subtractLessWeight(self, weights, uptoWeight):
    	if len(weights) != 0:
    		if uptoWeight + weights[0] < 200:
    			self.totalSubtractSum += uptoWeight + weights[0]
    			self.subtractLessWeight(weights[1:], uptoWeight + weights[0])
    		self.subtractLessWeight(weights[1:], uptoWeight)


    def comb(self, weights, index, uptoWeight):
    	for i in range(index+1, len(weights)):
    		if uptoWeight + weights[i] >= 200:
    			continue
    		else:
    			self.totalSubtractSum += uptoWeight + weights[i]
    			self.comb(weights, i, uptoWeight + weights[i]) 

    def theSum(self):
    	print(self.totalSubtractSum)
    	
    def solve(self, arr, isOne):
        # count = 0 
        # self.absolute = 0
        # firstLine = True
        # for line in fileinput.input():
        #     if firstLine:
        #         firstLine = False
        #         count = int(line.strip())
        #     else:
        #         absolute = 0
        #         weights = [int(i) for i in line.strip().split(" ")]
        #         self.fruitbasket(weights)
        self.fruitbasket(arr, isOne)
    def solve2(self, arr, isOne):
        self.fruitbasket(arr, isOne)
# solve = Solve().solve()


from random import randint
arr = []
for i in range(200):
	arr.append(randint(50, 200))
print(arr)
solve1 = Solve().solve(arr, True)

solve2 = Solve().solve2(arr, False)
