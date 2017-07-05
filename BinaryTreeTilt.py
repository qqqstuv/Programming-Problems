# https://leetcode.com/contest/leetcode-weekly-contest-29/problems/binary-tree-tilt/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def calculate(self, root, init):
        totalLeft = 0
        totalRight = 0
        # print(root.val, init)
        if root.left:
            [totalLeft, init] = self.calculate(root.left, init)
        if root.right:
            [totalRight,init] = self.calculate(root.right, init)
        diff = abs(totalRight - totalLeft)
        total = totalRight + totalLeft + root.val
        return [total, init + diff]
    
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        [maxTop, total] = self.calculate(root, 0)
        return total
