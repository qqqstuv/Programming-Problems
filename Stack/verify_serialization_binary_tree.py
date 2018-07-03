# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
# Idea: keeping a stack of each value along with left and right indication
# When encounter "#", if the parent is left, set it to right. If the parent is right. Recursively pop the stack with right indication and set the first left indication to right
class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        # print(preorder)
        stack = []
        if preorder[0] == '#':
            if len(preorder) > 1:
                return False
            else:
                return True
        stack.append([preorder.pop(0), "l"])
        idx = 0
        while len(stack) != 0:
            if idx >= len(preorder):
                return False

            node = preorder[idx]
            if node == "#":
                parent = stack.pop()
                if parent[1] == 'l':
                    parent[1] = "r"
                    stack.append(parent)
                else:
                    while(len(stack) != 0):
                        node = stack.pop()
                        if node[1] != 'r':
                            node[1] = 'r'
                            stack.append(node)
                            break
            else:
                stack.append([preorder[idx], "l"])
            idx += 1
        if idx != len(preorder):
            return False
        return True
        