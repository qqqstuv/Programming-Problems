#https://leetcode.com/problems/score-of-parentheses/description/
class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for i in S:
            if i == '(':
                stack.append(i)
            else:
                total = 0
                while(stack[-1] != '('):
                    total += stack.pop()
                stack.pop()
                if total != 0:
                    stack.append(total * 2)
                else:
                    stack.append(1)
                print(stack)
        return sum(stack)