#.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.



class TripleSteps(object):

    memo = dict()

    def possibleWaysAt(self, n):
        if n == 0:
            return 1
        if n in self.memo:
            return self.memo[n]
        stepThree = 0
        if n >= 3:
            stepThree += self.possibleWaysAt(n - 3) 
        stepTwo = 0
        if n >= 2:
            stepTwo += self.possibleWaysAt(n - 2)
        stepOne = 0
        if n >= 1:
            stepOne += self.possibleWaysAt(n - 1)
        totalSteps = stepOne + stepTwo + stepThree
        self.memo[n] = totalSteps

    def count(self, n):
        for i in range(1, n + 1):
            self.possibleWaysAt(i)
        print(self.memo[n])


tripleSteps = TripleSteps().count(10)
