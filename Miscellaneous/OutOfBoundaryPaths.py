
# Leetcode contest week 31 Question 4

class Solution(object):
    m = 40
    n = 40
    N = 50
    i = 0
    j = 0
    

    # a is height, b is width
    def calculateOutOfBound(self, a, b):
        count = 0
        if a + 1 >= self.m:
            count += 1
        if a - 1 < 0:
            count += 1
        if b + 1 >= self.n:
            count += 1
        if b - 1 < 0:
            count += 1
        return count

    def getPossibleMoves(self, a, b):
        possibleMoves = []
        if a + 1 < self.m:
            possibleMoves.append([a + 1,b])
        if a - 1 >= 0:
            possibleMoves.append([a - 1,b])
        if b + 1 < self.n:
            possibleMoves.append([a,b + 1])
        if b - 1 >= 0:
            possibleMoves.append([a,b - 1])
        return possibleMoves

    def pathsForMovementLeft(self, a,b, moveNum):
        localPaths = 0
        if moveNum == 0:
            return 0
        if moveNum == 1:
            localPaths += self.calculateOutOfBound(a,b) # base case
            # print("# of move with a b", a,b,localPaths)
        else:
            if self.memo[a][b].get(moveNum): # return a cached number
                return self.memo[a][b].get(moveNum)
            possibleMoves = self.getPossibleMoves(a,b)
            for move in possibleMoves:
                # print(move, moveNum - 1)
                localPaths += self.pathsForMovementLeft(move[0], move[1], moveNum - 1)

        self.memo[a][b][moveNum] =  localPaths #Update total
        return localPaths

    def operate(self):
        self.memo = [[dict() for i in range(self.n)] for j in range(self.m)]
        TOTAL = 0
        for moves in range(self.N + 1):
            print("moves", moves)
            localTotal = self.pathsForMovementLeft(self.i,self.j, moves)
            # print("total with such move", localTotal)
            TOTAL += localTotal
        print("TOTAL", TOTAL)
        # print(self.memo)

solution = Solution()
solution.operate()

