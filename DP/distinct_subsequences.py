#https://leetcode.com/problems/distinct-subsequences/description/
# DP Solution for this problem. Got Memory Limit Exceeded. There is a DP solution that works.
class Solution:
    def recur(self, s, t):
        if len(t) == 0:
            return 1
        if len(s) == 0:
            return 0
        key = str(len(s)) + "-" + str(len(t))
        if key in self.memo:
            return self.memo[key]
        total = 0
        if s[0] == t[0]:
            total = self.recur(s[1:], t) + self.recur(s[1:], t[1:])
        else:
            total = self.recur(s[1:], t)
        self.memo[key] = total
        return total
    
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        self.memo = dict()
        total = self.recur(s,t)
        return total