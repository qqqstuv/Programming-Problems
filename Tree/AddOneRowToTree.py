#Add One Row to Tree 
#https://leetcode.com/contest/leetcode-weekly-contest-37/problems/add-one-row-to-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        self.v = v
        self.d = d
        root = self.printLevelOrder(root)
        return root
        
    # Function to  print level order traversal of tree
    def printLevelOrder(self, root):
        if self.d == 1:
            print("ONE")
            temp = TreeNode(self.v)
            temp.left = root
            root = temp
            return root
        else:
            self.printGivenLevel(root, 1)
            return root
     
     
    # Print nodes at a given level
    def printGivenLevel(self, root , level):
        if root is None:
            return
        if level == self.d - 1:
            print (root.val)
            temp = TreeNode(self.v)
            if root.left is not None:
                temp.left = root.left
            root.left = temp
            temp = TreeNode(self.v)
            if root.right is not None:
                temp.right = root.right
            root.right = temp
        else:
            self.printGivenLevel(root.left , level+1)
            self.printGivenLevel(root.right , level+1)