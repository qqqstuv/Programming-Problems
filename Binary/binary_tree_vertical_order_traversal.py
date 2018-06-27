#https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
class Solution:
    
    def getHeight(self, root):
        if root:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        else:
            return 0
        
    def visit(self, root, k):
        if root:
            hashMap = dict()
            hashMap[0] = [(root.val, k)]
            leftMap = self.visit(root.left, k + 1)
            for key,val in leftMap.items():
                # print(val)
                if key - 1 in hashMap:
                    hashMap[key - 1] += val
                else:
                    hashMap[key - 1] = val
                
            rightMap = self.visit(root.right, k + 1)
            for key,val in rightMap.items():
                if key + 1 in hashMap:
                    hashMap[key + 1] += val
                else:
                    hashMap[key + 1] = val
            return hashMap
        else:
            return dict()
                
    
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        height = self.getHeight(root)
        ans = []
        hashMap = self.visit(root, 0)
        for key in sorted(hashMap.keys()):
            ans.append(hashMap[key])
        final = []
        for aList in ans:
            # aList = aList[0]
            # print(aList)
            aList = sorted(aList, key = lambda x : x[1])
            final.append([i[0] for i in aList])
        return final
            