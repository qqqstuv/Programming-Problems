class Solution:
    def traverse(self, root, height, current):
        if root:
            if height not in self.heights:
                self.heights[height] = [current,current]
            else:
                self.heights[height][1] = max(self.heights[height][1], current)
            if current > 0:
                self.traverse(root.left, height + 1, (current) * 2 - 1)
                self.traverse(root.right, height + 1, (current) * 2)
            else:
                self.traverse(root.left, height + 1, (current) * 2)
                self.traverse(root.right, height + 1, (current) * 2 + 1)
    
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.heights = dict()
        # self.heights[0] = [1,1]
        self.traverse(root.left, 1, -1)
        self.traverse(root.right, 1, 1)
        
        print(self.heights)
        ans = 1
        for val in self.heights.values():
            left = val[0]
            right = val[1]
            if left * right < 0:
                ans = max(ans, abs(left - right))
            else:
                ans = max(ans, abs(abs(right) - abs(left)) + 1)
                
        return ans