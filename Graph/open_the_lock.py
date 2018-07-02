#https://leetcode.com/problems/open-the-lock/description/
class Solution:
    
    def getNext(self, num):
        num = [int(i) for i in list(num)]
        ans = []
        ans.append([(num[0] + 1) %10, num[1], num[2], num[3]])
        ans.append([(num[0] - 1) %10, num[1], num[2], num[3]])
        ans.append([num[0], (num[1] + 1) %10, num[2], num[3]])
        ans.append([num[0], (num[1] - 1) %10, num[2], num[3]])
        ans.append([num[0], num[1], (num[2] + 1) %10, num[3]])
        ans.append([num[0], num[1], (num[2] - 1) %10, num[3]])
        ans.append([num[0], num[1], num[2], (num[3] + 1) %10])
        ans.append([num[0], num[1], num[2], (num[3] - 1) %10])
        for i in range(len(ans)):
            ans[i] = "".join([str(j) for j in ans[i]])
        # print(ans)
        return ans
        
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        visited = set()
        queue = [["0000",0]]
        while(len(queue) != 0):
            node,length = queue.pop(0)
            # print(node)
            if node in visited:
                continue
            visited.add(node)
            if node == target:
                return length
            if node not in deadends:
                nextNode = self.getNext(node)
                for newNode in nextNode:
                    if newNode not in deadends and newNode not in visited:
                        queue.append([newNode, length + 1])
            
        return -1
        