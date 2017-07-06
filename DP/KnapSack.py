import sys

class KnapSack(object):
    def __init__(self, value, weight, maxWeight):
        self.value = value
        self.weight = weight
        self.maxWeight = maxWeight


    def knapsack(self, values, weights, n, weightsLeft):
        print(values[n], weights[n], n,  weightsLeft)
        if n < 0 or weightsLeft == 0:
            return 0
        if weightsLeft < 0:
            return - sys.maxsize
        include = values[n] + self.knapsack(values, weights, n - 1, weightsLeft - weight[n])
        exclude = self.knapsack(values, weights, n - 1,  weightsLeft)
        return max(include, exclude)


    def KnapSack(self):
        total = self.knapsack(self.value, self.weight, len(value) - 1, self.maxWeight)
        print(total)

value = [20,5,10,40,15,25]

weight = [1,2,3,8,7,4]

maxWeight = 10

KnapSack(value, weight, maxWeight).KnapSack()

