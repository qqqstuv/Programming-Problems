#https://leetcode.com/problems/score-of-parentheses/description/
class Solution(object):

    def rescursiveSolve(self, S):
        if S[0] == '(':                
            if S[1] == ')':
                return 1
            else: # '('
                openBracketCount = 0
                start = 0
                total = 0
                S = S[1:-1]
                for i in range(len(S)):
                    if S[i] == '(':
                        openBracketCount += 1
                    else:
                        openBracketCount -= 1
                    if openBracketCount  == 0:
                        print(total)
                        total += self.rescursiveSolve(S[start:i+1])
                        start = i+1  
                return total  * 2
        
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if len(S) == 0:
            return 0
        S = '(' + S + ')'
        ans = self.rescursiveSolve(S)
        # print(ans)
        return(ans / 2)
        