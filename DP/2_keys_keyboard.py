# https://leetcode.com/problems/2-keys-keyboard/description/
# this is more like a math problem but it can be solved with DP. Solution is however slow though. Still a pass
import sys
class Solution:

    def recur(self, n, n_copied, copied, count):
        key = str(n) +"-"+ str(n_copied) + "-" + str(copied)
        if key in self.memo:
            return -1
        self.memo.add(key)
        if n > self.n:
            return -1
        if n == self.n:
            self.count = min(self.count, count)
        if not copied:
            self.recur(n, n, True, count + 1)
        self.recur(n + n_copied, n_copied, False, count + 1)
        
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        if n == 1:
            return 0
        self.memo = set()
        self.count = sys.maxsize
        self.recur(1,1, True, 1)
        return self.count   

ans = []
for i in range(1, 40):
    ans.append(Solution().minSteps(i))
print(ans)