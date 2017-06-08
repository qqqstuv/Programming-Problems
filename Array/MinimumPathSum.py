from collections import deque

class Input(object):
    """docstring for Input"""
    def __init__(self, matrix):
        self.matrix = matrix
        self.length = len(matrix)
        self.width = len(matrix[0])

    #coord: [y,x]
    def neighbors(self, coord):
        neighbors = []
        if coord[0] + 1 < self.length:
            neighbors.append([coord[0] + 1, coord[1]])
        if coord[1] + 1 < self.width:
            neighbors.append([coord[0], coord[1] + 1])
        return neighbors

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        origin = grid
        if len(origin) == 1 and len(origin[0]) == 1:
            # print( origin[0][0])
            return origin[0][0]
        
        queue = deque()
        
        input = Input(origin)
        queue.append([0,0])
        
        best = [[99999 for y in range(0,input.width)] for i in range(0,input.length)]
        best[0][0] = origin[0][0]
        while len(queue) != 0:
            node = queue.popleft()
            neighbors = input.neighbors(node) # get neighbors of node
            for neighbor in neighbors:
                # if best[neighbor[0]][neighbor[1]] != -1:
                current = best[neighbor[0]][neighbor[1]]
                parent = best[node[0]][node[1]]
                nodeVal = origin[neighbor[0]][neighbor[1]]
                newVal = current if parent + nodeVal > current else  parent + nodeVal
                # print("Index", neighbor[0],neighbor[1], "current", current,"parent", parent)
                best[neighbor[0]][neighbor[1]] = newVal
                queue.append(neighbor)
        # print(best[input.length - 1][input.width - 1])
        return best[input.length - 1][input.width - 1]
        




