# https://leetcode.com/contest/leetcode-weekly-contest-35/problems/construct-string-from-binary-tree/
class Solution:
    def tree2str(self, input):
        """
        :type input: array
        :rtype: str
        """
        if not input:
            input = [1,2,3,9,4,5,3,6,7,8,9,10,'null',999]
        level = 0
        levelOrder = []
        currentLevel = []
        count = 0
        for idx, val in enumerate(input):
            if count < 2**level:
                currentLevel.append(val)
                count += 1
                if idx == len(input) - 1:
                    levelOrder.append(currentLevel)
            else:
                levelOrder.append(currentLevel)
                currentLevel = []
                currentLevel.append(val)
                count = 1
                level += 1
        
        print(levelOrder)
        
        pair = []
        pairlist = []
        pairWrapper = []
        
        concatPair = [] # has setup pairs from the last layer [(3),(3)]

        for index, aLevel in enumerate(reversed(levelOrder)):
            for index,element in enumerate(aLevel):
                if element == 'null':
                    pair.append('(' + "" + ')')
                elif len(concatPair): # if lower layer
                    if index < len(concatPair): # if the node has children
                        children = ""
                        for e in concatPair[index]:
                            children += str(e)
                        # print('concatPair[index]', concatPair[index])
                        # print('children', children)
                        pair.append('(' + str(element) +  children + ')')
                    else:
                        pair.append('(' + str(element) + ')')
                else:
                    pair.append('(' + str(element) + ')')
        
                if len(pair) == 2:
                    pairlist.append(pair)
                    pair = []
                elif len(pair) == 1 and index == len(aLevel) - 1:
                    pairlist.append(pair)
                    pair = []
                # print("pairlist",pairlist)
            concatPair = pairlist
            pairlist = []
        return concatPair[0]
