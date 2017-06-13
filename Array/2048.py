

import sys


class LineObject():
    def __init__(self, order, graph): # order will be shifted
        self.order = order
        self.graph = graph

    def getRow(self, row):
        if self.order == 0: # left traverse
            return self.graph[row][::-1]
        elif self.order == 2: # # right traverse
            return self.graph[row]
        elif self.order == 1: # up traverse
            line = []
            for x in reversed(range(0,4)):
                line.append(self.graph[x][row])
            return line
        elif self.order == 3: # down traverse
            line = []
            for x in range(0,4):
                line.append(self.graph[x][row])
            return line

    def getGraph(self):
        return self.graph

    def reconvert(self, row, data):
        if self.order == 0: # left traverse
            self.graph[row] = data[::-1]
        elif self.order == 2: # # right traverse
            self.graph[row] = data
        elif self.order == 1: # up traverse
            for x in reversed(range(0,4)):
                self.graph[x][row] = data[abs(3 - x)]
        elif self.order == 3: # down traverse
            for x in range(0,4):
                self.graph[x][row] = data[x]
        
def shift(test, index):
    for i in reversed(range(0, index)): # 3 2 1 0 or 2 1 0 or 1 0
        test[i + 1] = test[i]
    test[0] = -1


def stripZero(test, index):
    if index == 0 or test[index] == -1:
        return test
    else:
        if test[index] == 0:
            shift(test, index)
            stripZero(test, index)
        else:
            stripZero(test, index - 1)

def replace(test):
    for idx, val in enumerate(test):
        if val == -1:
            test[idx] = 0

def perform(test, index):
    stripZero(test, 3)
    replace(test)
    add(test,3)
    return test

def add(test, index):
    if index == 0 or test[index] == 0 or test[index] == -1:
        replace(test)
        return test
    else:
        # print(test,index)
        if index != 0 and test[index] == test[index - 1]:
            test[index] = test[index - 1] * 2
            shift(test, index - 1)
        return add(test, index - 1)

input = [
            [2, 0, 0, 2],
            [4, 16, 8, 2],
            [2, 64, 32, 4],
            [1024, 1024, 64, 0]
        ]

count = 0

game = []
for line in sys.stdin:
    if count < 4:
        game.append([int(i) for i in line.split()])
        count += 1
    else:
        count = int(line)

# print(game)
lineObject = LineObject(count, game)

result = []
for i in range(0, 4):
    # print(lineObject.getRow(i))
    result.append(perform(lineObject.getRow(i),3))

for i in range(0,4):
    lineObject.reconvert(i, result[i])

answer = lineObject.getGraph()
for i in answer:
    print(*i)