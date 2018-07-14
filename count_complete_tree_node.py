#https://leetcode.com/problems/count-complete-tree-nodes/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def get_left(self, root):
        height = 0
        while root != None:
            height += 1
            root = root.left
        return height
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        height = self.get_left(root)
        node = root
        total = 0
        depth = 1
        last_level_max_node = 2 ** (height - 1)
        
        while depth < height:
            left = self.get_left(node.left)
            right = self.get_left(node.right)
            if left == right:
                node = node.right
                total += last_level_max_node // (2 **depth)
            else: # left = right + 1
                node = node.left
            depth += 1
        total += 1
        for i in range(1, height):
            total += 2 ** (i - 1)
        return total
